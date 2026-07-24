# 4.2 — Độ trễ và chi phí là chỉ số hạng nhất

[:material-notebook: Mở prompt_caching trên Colab](https://colab.research.google.com/github/anthropics/claude-cookbooks/blob/main/misc/prompt_caching.ipynb){ .md-button }

!!! abstract "Mục tiêu"
    - Đọc ngân sách độ trễ bằng p50/p95/p99, không bằng trung bình.
    - Phân biệt thời gian tới token đầu tiên và thời gian hoàn tất.
    - Tính chi phí mỗi truy vấn đủ cả nhúng, xếp hạng lại, và lượt gọi lặp.

## Vì sao trung bình là con số vô dụng

<div class="predict" markdown>
**Dự đoán:** Hệ thống của bạn có độ trễ trung bình 800ms. Dự đoán: con số này nói cho bạn biết gì về trải
nghiệm của người dùng chậm nhất?

<textarea class="predict-input" placeholder="Viết dự đoán của bạn — dài ít nhất một câu..."></textarea>
<button class="predict-btn">Mở kết quả</button>

<div class="predict-result" hidden markdown>
**Gần như không gì cả.** Trung bình che mất đuôi. Một hệ 800ms trung bình có thể có `p99` = 12 giây — tức 1%
người dùng chờ 12 giây. Chính cái đuôi đó quyết định họ có bỏ đi không. Luôn đọc **percentile** (p50/p95/p99),
không bao giờ chỉ đọc trung bình.
</div>
</div>

```python
def percentile(values, p):
    s = sorted(values)
    k = (len(s) - 1) * p / 100
    lo = int(k)
    if lo == k or lo + 1 >= len(s):
        return s[lo]
    return s[lo] + (s[lo + 1] - s[lo]) * (k - lo)   # nội suy tuyến tính

lat = [t["latency_ms"] for t in traces]
print("p50", percentile(lat, 50), "p95", percentile(lat, 95), "p99", percentile(lat, 99))
```

## Token đầu tiên vs hoàn tất

Người dùng cảm nhận **thời gian tới token đầu tiên** (TTFT) khi có streaming — màn hình bắt đầu chạy chữ — chứ
không phải thời gian hoàn tất. Một câu trả lời dài nhưng TTFT nhanh *cảm giác* nhanh hơn một câu ngắn TTFT chậm.
Đo và tối ưu đúng cái người dùng cảm nhận.

## Chi phí mỗi truy vấn

Tính đủ: input tokens + output tokens của **mọi** lượt gọi (agent lặp nhiều lượt), cộng nhúng (embedding) và
xếp hạng lại nếu có. Một agent 5 bước tốn ~5× so với một lượt.

## Prompt caching — đòn bẩy chi phí/độ trễ

Với phần context lặp lại (system prompt dài, tài liệu cố định), đánh dấu `cache_control` để tái dùng, giảm cả
chi phí lẫn độ trễ:

```python
r = client.messages.create(
    model="claude-sonnet-5", max_tokens=1024,
    system=[{"type": "text", "text": LONG_SYSTEM,
             "cache_control": {"type": "ephemeral"}}],   # cache phần này
    messages=[{"role": "user", "content": cau_hoi}],
)
```

<div class="tool-justify" markdown>
**Thẻ biện minh — prompt caching**

- **Thay bằng gì vẫn chạy?** Gửi lại full context mỗi lần.
- **Gỡ ra thì chỉ số nào tụt?** Chi phí input tokens và độ trễ với context lặp lớn — nhưng thêm rủi ro **cache
  vô hiệu hoá**: nếu context đổi nhẹ, cache miss, và một lần *trúng cache sai* (trả context cũ) là lỗi nguy hiểm.
</div>

??? note "Đi sâu — batch cho tác vụ không cần real-time"
    Tác vụ nền (đánh giá lại toàn corpus, sinh nhãn) không cần độ trễ thấp → dùng [batch](https://colab.research.google.com/github/anthropics/claude-cookbooks/blob/main/misc/batch_processing.ipynb)
    để giảm chi phí đáng kể, đổi lấy độ trễ cao.

## Lỗi thường gặp

- Báo cáo trung bình thay vì percentile → giấu cái đuôi.
- Quên cộng lượt gọi lặp của agent vào chi phí.
- Cache context động → trúng cache sai, trả dữ liệu cũ.

## Tóm tắt

Đọc p50/p95/p99; tối ưu TTFT; tính chi phí đủ mọi lượt gọi; dùng caching cho context lặp nhưng canh cache
invalidation.

→ Tiếp: [4.3 — Bảo mật và chống thoái lui](../4.3-bao-mat/bai-giang.md)
