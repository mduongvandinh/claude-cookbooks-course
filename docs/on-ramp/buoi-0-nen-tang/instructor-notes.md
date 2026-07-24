# Instructor notes — Buổi 0

**Thời lượng:** ~90 phút (dài hơn buổi thường vì lớp hỗn hợp; người có kinh nghiệm có thể rời sớm sau phần 2).

## Thông điệp chốt

1. Tool use là **vòng lặp hai chiều**: model chỉ *yêu cầu*, code của bạn mới *chạy* tool.
2. `stop_reason` là tín hiệu điều khiển — đọc sai nó là bỏ lỡ toàn bộ nhánh tool.
3. Structured output không cần chạy tool — chỉ đọc `input`. Đây là mẹo dùng suốt Trục 00/02.

## Câu hỏi gợi mở

- "Nếu không gửi `tool_result` trở lại thì chuyện gì xảy ra?" (model không bao giờ thấy kết quả → không trả lời được).
- "Ai thực sự chạy tool — Claude hay code của bạn?" (câu này nạp vào bộ câu hỏi vàng).
- "Vì sao dùng tool để lấy JSON thay vì bảo Claude trả JSON trong text?" (đảm bảo đúng schema, parse chắc chắn).

## Điểm người mới hay vấp

- Nhầm `msg.content` là chuỗi — nó là **danh sách khối**, phải lấy `content[0].text`.
- Quên đính lượt `assistant` (`r.content`) vào lịch sử trước `tool_result`.
- Bối rối giữa `tool_use` (model yêu cầu) và `tool_result` (bạn trả lời).

## Gợi ý demo live

Chạy phần 2 với số lớn, cố tình **bỏ** `tool_use_id` để lớp thấy lỗi API thật, rồi thêm lại. Đây cũng là bản
xem trước cho "bài phá trước" ở Trục 00.

## Nạp vào bộ câu hỏi vàng

- "Ai thực sự chạy tool — Claude hay code của bạn?"
- "Khi nào dùng `tool_choice` = `tool` thay vì `auto`?"
