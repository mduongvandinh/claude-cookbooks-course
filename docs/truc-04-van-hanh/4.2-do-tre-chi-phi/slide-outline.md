# Slide outline — Buổi 4.2

### Slide 1 — Tựa
4.2 Độ trễ và chi phí là chỉ số hạng nhất.

### Slide 2 — Trung bình nói dối
800ms trung bình có thể p99 = 12 giây.

### Slide 3 — Percentile
p50/p95/p99. Cái đuôi quyết định người dùng bỏ đi.

### Slide 4 — TTFT vs hoàn tất
Người dùng cảm nhận token đầu tiên (khi streaming).

### Slide 5 — Chi phí mỗi truy vấn
Đủ mọi lượt gọi + nhúng + rerank. Agent 5 bước ≈ 5×.

### Slide 6 — Prompt caching
`cache_control` cho context lặp. Rủi ro cache invalidation.

### Slide 7 — Batch cho tác vụ nền
Không cần real-time → batch rẻ hơn, đổi lấy độ trễ.

### Slide 8 — Lỗi thường gặp + Tóm tắt
Báo cáo trung bình; quên lượt lặp; cache context động.

---

**Cheat sheet 1 dòng:** đọc p50/p95/p99 (không mean) → tối ưu TTFT → chi phí đủ mọi lượt → cache context lặp (canh invalidation).
