# Lời giải — Buổi 2.3

## Core — Hai chỉ số từ chối
```python
tu_choi_dung = refuse_count(answers_out_of_scope) / len(answers_out_of_scope)
tu_choi_nham = refuse_count(answers_in_scope) / len(answers_in_scope)
# Thêm grounding prompt -> tu_choi_dung tăng, thường tu_choi_nham cũng tăng (kéo nhau)
```
**Rubric:** hai cặp số trước/sau (2đ); nhận xét kéo nhau (1đ).

## Đi sâu — Tín hiệu trích dẫn
Từ chối khi `not any(block.citations ...)` thường cân bằng hơn prompt thuần vì có bằng chứng khách quan.
**Rubric:** so sánh hai cách (2đ); kết luận đúng (1đ).

## Capstone — Cổng 02
**Rubric:** trung thành ≥ 0.80 + từ chối đúng ≥ 70% + nhầm ≤ 10% (3đ); ca vẫn sai + nguyên nhân (1đ).
