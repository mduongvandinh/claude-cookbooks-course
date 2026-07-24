# Bài tập — Buổi 0

## Core — Chặn chia cho 0

**Dự đoán trước:** nếu người dùng hỏi "10 chia 0 bằng mấy?", chương trình ở bài giảng sẽ làm gì khi `eval`
gặp `10/0`?

Nhiệm vụ: sửa hàm chạy tool để **không crash** khi biểu thức không hợp lệ (chia 0, cú pháp sai) — trả về một
thông báo lỗi dạng chuỗi để gửi lại cho model.

**Tiêu chí đạt:** hỏi "10 chia 0" không làm chương trình dừng; model nhận được thông báo lỗi và trả lời gọn.

## Đi sâu — Structured output có field lồng nhau

**Dự đoán trước:** nếu schema có một object lồng (ví dụ `author` gồm `name` và `email`), Claude có điền đủ cả
hai field con không khi bạn ép `tool_choice`?

Nhiệm vụ: định nghĩa tool `save_contact` với `input_schema` có object lồng `author {name, email}`, ép gọi
bằng `tool_choice`, và in ra `input`.

**Tiêu chí đạt:** `input` trả về đúng cấu trúc lồng, có cả `name` và `email`.

## Bước capstone — Khởi tạo trợ lý

Tạo file `tro_ly.py`: một chatbot đơn giản dùng **một** tool (calculator), theo đúng vòng 4 bước. Đây là nền
cho "Trợ lý tài liệu nội bộ" — capstone sẽ lớn dần qua các trục.

**Tiêu chí đạt:** `tro_ly.py` chạy được, trả lời một câu hỏi có dùng tool.
