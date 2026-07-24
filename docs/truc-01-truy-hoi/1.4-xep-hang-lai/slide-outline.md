# Slide outline — Buổi 1.4

### Slide 1 — Tựa
1.4 Xếp hạng lại và bài toán ngân sách.

### Slide 2 — Bao phủ vs chính xác
Lấy rộng (top-50) rồi rerank xuống top-k.

### Slide 3 — Reranker Claude
Prefill `<relevant_indices>` + stop_sequences. 78% → 85%.

### Slide 4 — Reranker Cohere
`rerank-english-v3.0` — nhanh hơn.

### Slide 5 — Chất lượng vs độ trễ
Buổi đầu tiên hai thứ cạnh nhau. Cầu nối sang Trục 04.

### Slide 6 — Bảng đóng góp
Mỗi kỹ thuật: điểm thêm | ms thêm. Đo trước/sau.

### Slide 7 — Lỗi thường gặp + Tóm tắt
Bật rerank không đo ms; dùng Claude khi Cohere đủ.

---

**Cheat sheet 1 dòng:** lấy rộng → rerank (Claude/Cohere) → bảng đóng góp (điểm|ms) → Cổng 01.
