# Lời giải — Buổi 2.2

## Core — Lost-in-the-middle
```python
for pos in [0, 4, 9, 14, 19]:
    ctx = chunks_other[:pos] + [chunk_correct] + chunks_other[pos:]
    acc[pos] = eval_answers(ctx)   # tỉ lệ đúng khi chunk đúng ở vị trí pos
# Kỳ vọng: cao ở 0 và 19, thấp ở giữa (chữ U)
```
**Rubric:** đường cong theo vị trí (2đ); nhận xét chữ U (1đ).

## Đi sâu — Phân xử
```python
system = ("Khi tài liệu mâu thuẫn, ưu tiên phiên bản mới hơn (trường 'version'); "
          "nếu không xác định được, nêu rõ mâu thuẫn thay vì chọn bừa.")
```
**Rubric:** tỉ lệ chọn đúng phiên bản trước/sau (3đ).

## Capstone
**Rubric:** phân xử kiểm chứng được (2đ); số chunk theo điểm gãy (1đ).
