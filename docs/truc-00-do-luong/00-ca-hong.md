# Ca hỏng mở màn — Giám khảo hỏng

!!! danger "Bắt đầu bằng cái hỏng (quy tắc ②)"
    Trục này không mở màn bằng một bộ chấm chạy đúng, mà bằng một bộ chấm **đang cho ra kết luận sai**. Nhiệm vụ
    của bạn: tìm ra nó sai ở đâu, trước khi học cách làm đúng.

## Bối cảnh

Bạn phát cho lớp một bộ chấm dạng **so sánh cặp**: đưa hai câu trả lời A và B, giám khảo (model) chọn cái tốt
hơn. Trên **200 cặp**, cấu hình A thắng **65%**. Học viên kết luận: cấu hình A tốt hơn.

Đây là code họ dùng (bản đầy đủ: `docs/assets/broken/giam_khao_hong.py`):

```python
from anthropic import Anthropic
import re

client = Anthropic()
MODEL_NAME = "claude-sonnet-5"

def judge_once(question, answer_first, answer_second):
    prompt = (
        f"Câu hỏi: {question}\n"
        f"Câu trả lời A: {answer_first}\n"
        f"Câu trả lời B: {answer_second}\n"
        "Câu nào tốt hơn? Chỉ xuất 'A' hoặc 'B' trong <winner></winner>."
    )
    out = client.messages.create(
        model=MODEL_NAME, max_tokens=256,
        messages=[{"role": "user", "content": prompt}],
    ).content[0].text
    m = re.search(r"<winner>(.*?)</winner>", out, re.DOTALL)
    return m.group(1).strip()

def run(pairs):
    # LỖI: luôn đặt cấu hình A ở vị trí đầu, cấu hình B ở vị trí sau — không hoán đổi.
    wins_a = 0
    for question, ans_a, ans_b in pairs:
        if judge_once(question, ans_a, ans_b) == "A":
            wins_a += 1
    return wins_a / len(pairs)
```

## Bài phá trước

<div class="predict" markdown>
**Dự đoán:** Bạn yêu cầu họ chạy lại **đúng 200 cặp đó** nhưng **hoán đổi vị trí** A và B (A giờ hiển thị ở chỗ
thứ hai). Dự đoán điều gì sẽ xảy ra với tỉ lệ thắng?

<textarea class="predict-input" placeholder="Viết dự đoán của bạn — dài ít nhất một câu..."></textarea>
<button class="predict-btn">Khoá dự đoán & xem kết quả</button>

<div class="predict-result" hidden markdown>
Tỉ lệ thắng của **vị trí thứ nhất** gần như không đổi — vẫn quanh 60–65% — dù nội dung A và B đã hoán chỗ
hoàn toàn. Cái bạn đo được **không phải chất lượng của A**, mà là **thiên lệch vị trí (position bias)** của
giám khảo: model có xu hướng chọn câu xuất hiện trước.

**Lỗi cụ thể trong code:** `run()` luôn đặt cấu hình A ở vị trí đầu, B ở vị trí sau — không bao giờ hoán đổi.
Nên nó đo lẫn cả position bias vào "tỉ lệ thắng của A".

**Bản sửa — chạy cả hai chiều rồi tổng hợp:**

```python
def judge_pair_debiased(question, ans_a, ans_b):
    v1 = judge_once(question, ans_a, ans_b)   # A ở vị trí đầu
    v2 = judge_once(question, ans_b, ans_a)   # A ở vị trí sau (giờ A là "B")
    picks_a = (v1 == "A") + (v2 == "B")       # số lần thật sự chọn ans_a
    if picks_a == 2: return "A"
    if picks_a == 0: return "B"
    return "hoà"   # bất đồng giữa hai chiều = tín hiệu câu khó / giám khảo yếu
```

Hoặc đơn giản hơn: bỏ so cặp, chuyển sang **chấm nhị phân từng câu** một theo rubric.
</div>
</div>

## Vì sao đây là cách vào bài

Trước khi tin bất kỳ con số nào, phải đo chính **cái thước**. Một giám khảo chưa được kiểm định thì mọi thí
nghiệm phía sau — mọi so sánh RAG, mọi bảng xếp hạng agent — đều vô hiệu. Đó là lý do Trục 00 đi trước tất cả.

Ghi ngay lỗi này vào [sổ lỗi & test case](../so-loi-test-case.md): "đo A vs B mà không hoán đổi vị trí".

→ Tiếp: [0.1 — Phân tích lỗi trước khi nghĩ tới chỉ số](0.1-phan-tich-loi/bai-giang.md)
