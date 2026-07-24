# 3.4 — Chấm agent

[:material-notebook: Mở evaluator_optimizer trên Colab](https://colab.research.google.com/github/anthropics/claude-cookbooks/blob/main/patterns/agents/evaluator_optimizer.ipynb){ .md-button }

!!! abstract "Mục tiêu"
    - Chấm kết quả cuối hay chấm cả đường đi — và khi nào kết quả đúng vẫn phải đánh trượt.
    - Phân biệt `pass@k` (khả năng) và `pass^k` (độ tin cậy).
    - Định vị lỗi trong vệt chạy dài bằng khung phân loại.

## pass@k vs pass^k

<div class="predict" markdown>
**Dự đoán:** Agent của bạn chạy đúng 8/10 lần cho một tác vụ. Với sản phẩm, con số nào quan trọng hơn: "ít nhất
một lần đúng" hay "mọi lần đều đúng"?

<textarea class="predict-input" placeholder="Viết dự đoán của bạn — dài ít nhất một câu..."></textarea>
<button class="predict-btn">Mở kết quả</button>

<div class="predict-result" hidden markdown>
**"Mọi lần đều đúng"** — tức `pass^k`. `pass@k` (ít nhất 1 trong k lần đúng) đo **khả năng**; `pass^k` (cả k lần
đều đúng) đo **độ tin cậy**. Người dùng sản phẩm gặp một lần chạy, không phải "lần tốt nhất trong 10". 8/10 nghe
ổn nhưng `pass^3` ≈ 0.8³ ≈ 0.51 — tức chạy 3 lần liên tiếp chỉ đúng cả ba khoảng 51%. Khoảng cách giữa `pass@k`
và `pass^k` cho biết agent của bạn *may rủi* đến mức nào.
</div>
</div>

`pass@k` và `pass^k` **không** có trong cookbook — đây là khái niệm chuẩn của ngành, tính từ nhiều lần chạy trên
cùng tác vụ. Cổng 03 yêu cầu báo cáo `pass^3`.

## Chấm kết quả vs chấm đường đi

Kết quả đúng vẫn có thể phải đánh trượt: agent gọi tool xoá nhầm rồi vô tình sửa lại → kết quả đúng nhưng đường
đi nguy hiểm. Chấm **cả đường đi** khi hành động có hệ quả (Trục 04).

## Vòng đánh giá trong khung chạy

evaluator_optimizer minh hoạ giám khảo-trong-vòng: sinh → đánh giá (PASS/NEEDS_IMPROVEMENT/FAIL) → sửa theo phản
hồi, lặp tới PASS:

```python
def loop(task, evaluator_prompt, generator_prompt):
    thoughts, result = generate(generator_prompt, task)
    while True:
        evaluation, feedback = evaluate(evaluator_prompt, result, task)
        if evaluation == "PASS":
            return result
        context = f"Các lần trước + phản hồi: {feedback}"
        thoughts, result = generate(generator_prompt, task, context)
```

!!! warning "Không có max-iteration"
    Vòng gốc lặp tới PASS, không giới hạn — ở sản xuất phải thêm `max_steps` để tránh vòng vô hạn/đốt chi phí.

## Cùng mô hình, khác khung chạy → thứ hạng đảo

Một hệ quả khó chịu: cùng một mô hình, đổi khung chạy (prompt, tool, cách lặp) có thể **đảo thứ hạng** so với mô
hình khác. Hệ quả: đừng tin mù bảng xếp hạng — chúng đo *mô hình + khung*, không chỉ mô hình.

<div class="tool-justify" markdown>
**Thẻ biện minh — chấm cả đường đi (không chỉ kết quả)**

- **Thay bằng gì vẫn chạy?** Chỉ chấm kết quả cuối.
- **Gỡ ra thì chỉ số nào tụt?** Khả năng bắt lỗi nguy hiểm mà kết quả cuối che giấu (hành động không đảo).
</div>

## Lỗi thường gặp

- Báo cáo `pass@k`, giấu `pass^k`.
- Chỉ chấm kết quả cuối khi hành động có hệ quả.
- Vòng lặp không có `max_steps`.
- Tin bảng xếp hạng như đo mô hình thuần.

## Tóm tắt

`pass^k` đo độ tin cậy (sản phẩm cần); chấm đường đi khi hành động có hệ quả; định vị lỗi bằng khung phân loại;
khung chạy đổi thứ hạng. Đây là cổng vào tư duy vận hành (Trục 04).

→ Tiếp: [Cổng 03](../cong-03.md)

---

**Tài liệu buổi này:** [Instructor notes](instructor-notes.md) · [Bài tập](bai-tap.md) · [Lời giải](loi-giai.md) · [Slide outline](slide-outline.md)
