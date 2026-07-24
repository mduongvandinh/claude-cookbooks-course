# Lời giải — Buổi 3.4

## Core — pass@k / pass^k
```python
# runs[task] = list các True/False qua k lần chạy
def pass_at_k(runs, k):   # ít nhất 1 trong k đúng
    return sum(any(r[:k]) for r in runs) / len(runs)
def pass_pow_k(runs, k):  # cả k đều đúng
    return sum(all(r[:k]) for r in runs) / len(runs)
# 8/10 mỗi lần -> pass^3 ≈ 0.8**3 ≈ 0.51
```
**Rubric:** hai con số (2đ); giải thích khoảng cách = độ tin cậy (1đ).

## Đi sâu — Chấm đường đi
```python
# max_steps chặn vòng vô hạn
for step in range(MAX_STEPS):
    if response.stop_reason != "tool_use": break
    ...
# tiêu chí đường đi: nếu gọi tool ghi khi câu hỏi chỉ cần đọc -> trượt dù kết quả đúng
```
**Rubric:** bắt được ca kết-quả-đúng-đường-sai (2đ); có max_steps (1đ).

## Capstone — Cổng 03
**Rubric:** acc chọn công cụ ≥ 0.80 (1đ); pass^3 báo cáo (1đ); chứng minh agent vs pipeline (1đ).
