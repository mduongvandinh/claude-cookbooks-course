# Bài tập — Buổi 4.1

## Core — Thêm vệt chạy có cấu trúc
**Dự đoán trước:** với hệ hiện tại, một khiếu nại "trả lời sai" — bạn cần bao lâu để lần ra lượt gọi?

Nhiệm vụ: thêm `new_trace`/`log_step` vào trợ lý capstone, ghi ít nhất các bước retrieve + generate + final.

**Tiêu chí đạt:** mỗi truy vấn sinh một trace có `trace_id` và ≥ 3 bước, lưu tra cứu được theo id.

## Đi sâu — Lần ngược bấm giờ
**Dự đoán trước:** field nào sẽ thiếu khiến bạn không phân biệt được lỗi truy hồi vs sinh?

Nhiệm vụ: cho một `trace_id`, lần ngược tới đúng lượt gọi trong < 2 phút; ghi lại field còn thiếu.

**Tiêu chí đạt:** lần ngược < 2 phút; danh sách field còn thiếu để bổ sung.

## Capstone — Vệt chạy cho trợ lý
Gắn vệt chạy vào "Trợ lý tài liệu nội bộ", đủ để chấm cả ba mặt (đầu ra/đường đi/trạng thái).

**Tiêu chí đạt:** trace chấm được cả ba mặt; không ghi nội dung tài liệu nặng.
