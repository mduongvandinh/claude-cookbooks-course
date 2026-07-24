# Slide outline — Buổi 1.2

### Slide 1 — Tựa
1.2 Chunking và siêu dữ liệu — hai đòn bẩy lớn nhất.

### Slide 2 — Câu hỏi sai
"Bao nhiêu token" là câu hỏi sai. "Tự đủ nghĩa không" mới đúng.

### Slide 3 — Chunk theo cấu trúc
Cắt ở ranh giới mục/khối mã, không cắt ngang đơn vị nghĩa.

### Slide 4 — Contextual retrieval
Gắn câu ngữ cảnh trước khi nhúng; cache tài liệu.

### Slide 5 — Kết quả
Pass@10 87% → 92% (điển hình).

### Slide 6 — Lọc metadata
Phiên bản/sản phẩm/ngày → lọc cứng trước xếp hạng.

### Slide 7 — Lỗi thường gặp + Tóm tắt
Cắt ký tự; bỏ metadata; sinh ngữ cảnh không cache.

---

**Cheat sheet 1 dòng:** chunk theo cấu trúc + gắn ngữ cảnh (cache) + lọc metadata cứng → tối ưu trước rerank.
