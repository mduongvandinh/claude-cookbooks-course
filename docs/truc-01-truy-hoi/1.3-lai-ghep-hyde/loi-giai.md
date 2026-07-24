# Lời giải — Buổi 1.3

## Core — Lai ghép
```python
# semantic_rank, bm25_rank: vị trí trong xếp hạng mỗi nguồn
score = 0.8 * (1 / (semantic_rank + 1)) + 0.2 * (1 / (bm25_rank + 1))
# Thử 0.8/0.2, 0.6/0.4, 0.5/0.5 -> chọn theo recall đo được trên nhóm mã lỗi
```
**Rubric:** recall trước/sau (2đ); trọng số chọn dựa trên đo (1đ).

## Đi sâu — HyDE
HyDE thường +recall trên nhóm mơ hồ, −recall/+độ trễ trên nhóm cụ thể. **Rubric:** hai con số hai nhóm (2đ);
kết luận đúng (1đ).

## Capstone
**Rubric:** recall tăng nhóm mã lỗi (2đ); bảng đóng góp cập nhật (1đ).
