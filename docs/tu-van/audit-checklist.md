# Checklist audit hệ thống LLM

Một **sản phẩm tư vấn bán được**: chấm hệ LLM của khách theo 5 cổng, mỗi trục 0-5 điểm, ra một bức tranh khách
quan trong một buổi. Đây cũng là "bước đầu tiên có giá" để mở đường cho hợp đồng lớn hơn.

!!! note "Cách chào"
    "Tôi đề xuất một buổi audit 2-3 giờ. Đầu ra là một báo cáo chấm hệ của anh theo 5 chiều, mỗi chiều một con số,
    kèm ba việc đáng làm nhất. Xong buổi đó anh có bức tranh khách quan để quyết định bước tiếp."

## Bảng chấm (0-5 mỗi trục)

Cho điểm theo mức đạt được, dựa trên tiêu chí *có thật, đo được*:

### Trục 00 — Đo lường
- [ ] **1** — Có đọc dữ liệu lỗi thật (không chỉ dashboard)
- [ ] **2** — Có bộ đề vàng ≥ 24 câu
- [ ] **3** — Bộ đề phủ đủ 6 loại (dữ kiện/phiên bản/biên/ngoài phạm vi/đối kháng/nhất quán)
- [ ] **4** — Giám khảo đạt Cohen κ ≥ 0.6 so với người
- [ ] **5** — Một lệnh CLI ra một con số, lặp lại chênh < 2%

### Trục 01 — Truy hồi
- [ ] **1** — Có baseline + đo recall@k
- [ ] **2** — Chunk theo cấu trúc (không cắt ký tự)
- [ ] **3** — Lọc metadata phiên bản/sản phẩm
- [ ] **4** — Tìm kiếm lai (embedding + từ khoá)
- [ ] **5** — Xếp hạng lại + bảng đóng góp (điểm | ms mỗi kỹ thuật)

### Trục 02 — Sinh
- [ ] **1** — Tách đo lỗi sinh khỏi lỗi truy hồi
- [ ] **2** — Đo trần phần sinh (context hoàn hảo)
- [ ] **3** — Trích dẫn kiểm chứng được (không phải prompt)
- [ ] **4** — Độ trung thành ≥ 0.90
- [ ] **5** — Từ chối đúng ≥ 80% & từ chối nhầm ≤ 5%

### Trục 03 — Vòng lặp
- [ ] **1** — Có lý do (đo được) cho việc dùng/không dùng agent
- [ ] **2** — Mô tả công cụ rõ ràng (không đồng nghĩa)
- [ ] **3** — Đo độ chính xác chọn công cụ ≥ 0.90
- [ ] **4** — Có `max_steps` + phân tầng trạng thái hợp lý
- [ ] **5** — Báo cáo pass^k, chấm cả đường đi

### Trục 04 — Vận hành
- [ ] **1** — Có vệt chạy có cấu trúc
- [ ] **2** — Lần ngược khiếu nại < 2 phút
- [ ] **3** — Biết p50/p95/p99 + chi phí mỗi truy vấn
- [ ] **4** — Kiểm bộ ba chết người + người duyệt hành động không đảo
- [ ] **5** — Eval tự động chặn regression trong CI

## Tổng điểm → chẩn đoán

| Tổng (25) | Chẩn đoán | Thông điệp cho khách |
|---|---|---|
| 0-8 | **Demo, chưa phải sản phẩm** | "Hệ chạy được nhưng chưa đo được — rủi ro cao khi có người dùng thật." |
| 9-15 | **Đang lên sản phẩm** | "Có nền, nhưng vài cổng còn hở — đây là ba việc đáng làm nhất." |
| 16-21 | **Sản phẩm ổn** | "Vững ở phần lõi, tinh chỉnh phần vận hành để chịu tải/tấn công." |
| 22-25 | **Chín** | "Ít việc để làm — tập trung tối ưu chi phí và mở rộng." |

## Đầu ra báo cáo (mẫu 1 trang)

1. **Điểm 5 trục** (radar hoặc bảng) + tổng.
2. **Ba lỗ hổng lớn nhất** — cổng nào hở, hậu quả cụ thể, cách chữa.
3. **Trục yếu nhất** = ưu tiên số một (thường là Trục 00 nếu chưa có eval).
4. **Một "quick win"** làm được trong 1 tuần.

!!! warning "Chấm trung thực = uy tín"
    Đừng chấm cao để lấy lòng. Một audit thẳng thắn (kèm lối ra rõ ràng) tạo niềm tin mạnh hơn lời khen. Khách
    thuê bạn vì bạn *thấy được* cái họ không thấy.
