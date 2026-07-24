# Lời giải — Buổi 1.2

## Core — Chunk theo cấu trúc
Cắt ở ranh giới mục/tiểu mục/khối mã (regex heading, fence ```); không cắt ngang đơn vị nghĩa. **Rubric:** hai
cặp số trước/sau (2đ); giải thích recall ~không đổi mà trung thành tăng (1đ).

## Đi sâu — Contextual + metadata
```python
text_to_embed = f"{contextualized_text}\n\n{chunk['content']}"   # gắn ngữ cảnh trước khi nhúng
# lọc cứng: chỉ giữ chunk có metadata['version'] == target trước khi xếp hạng
```
**Rubric:** Pass@10 trước/sau (2đ); truy vấn chứng minh lọc phiên bản (1đ).

## Capstone
**Rubric:** recall@10 tăng so với mốc 1.1 (2đ); bảng đóng góp 2 dòng (1đ).
