# Slide outline — Buổi 3.4

### Slide 1 — Tựa
3.4 Chấm agent.

### Slide 2 — pass@k vs pass^k
Khả năng vs độ tin cậy. Sản phẩm cần pass^k.

### Slide 3 — 8/10 nghe ổn?
pass^3 ≈ 0.51 — chạy 3 lần đúng cả ba chỉ ~51%.

### Slide 4 — Chấm kết quả vs đường đi
Kết quả đúng vẫn có thể phải đánh trượt.

### Slide 5 — Vòng đánh giá trong khung
evaluator_optimizer: sinh → đánh giá → sửa. Cần max_steps.

### Slide 6 — Khung chạy đổi thứ hạng
Cùng mô hình khác khung → thứ hạng đảo. Đừng tin mù bảng xếp hạng.

### Slide 7 — Lỗi thường gặp + Tóm tắt
pass@k giấu pass^k; không max_steps; tin leaderboard.

---

**Cheat sheet 1 dòng:** báo cáo pass^k (độ tin cậy) + chấm đường đi khi hành động có hệ quả + max_steps.
