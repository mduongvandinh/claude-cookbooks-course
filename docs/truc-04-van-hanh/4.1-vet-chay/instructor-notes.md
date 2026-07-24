# Instructor notes — Buổi 4.1

**Thời lượng:** ~60 phút.

## Thông điệp chốt
1. Ở sản xuất, thứ duy nhất còn lại sau sự cố là vệt chạy — không có nó = "không tái hiện được".
2. Ghi đầu vào quyết định + kết quả + thời gian; đừng ghi nội dung nặng/nhạy cảm.
3. Vệt chạy phải đủ để chấm cả ba mặt: đầu ra, đường đi, trạng thái cuối.

## Câu hỏi gợi mở
- "Field tối thiểu nào cần để phân biệt lỗi truy hồi vs lỗi sinh?" (doc_ids + phiên bản).
- "Ghi log gì thì thừa?" (nội dung tài liệu, dữ liệu nhạy cảm).

## Điểm hay vấp
- Log văn bản tự do → không truy vấn được. Thiếu `trace_id` xuyên suốt.

## Gợi ý demo
Bấm giờ: cho một `trace_id`, lần ngược tới lượt gọi model trong < 2 phút.

## Nạp bộ câu hỏi vàng
- "Người dùng chạy đúng code của bạn nhưng ra kết quả khác. Ba nguyên nhân khả dĩ?"
