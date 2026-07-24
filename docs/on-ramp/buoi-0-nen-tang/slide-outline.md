# Slide outline — Buổi 0

### Slide 1 — Tựa
Buổi 0: Gọi được Claude và một vòng tool use. On-ramp cho người mới.

### Slide 2 — Vì sao có buổi này
Trục 00 giả định bạn gọi được API + định nghĩa tool. Buổi này san bằng điểm xuất phát.

### Slide 3 — Gọi API cơ bản
`client.messages.create(...)`; `messages` là danh sách lượt; kết quả ở `content[0].text`.

### Slide 4 — Vấn đề: Claude không tự tính số lớn
Demo: hỏi "1984135 * 9343116" → nó nhờ tool.

### Slide 5 — Bốn bước vòng tool use
(a) gọi với `tools=` → (b) `stop_reason == "tool_use"` → (c) chạy tool → (d) gửi `tool_result`.

### Slide 6 — Ai chạy tool?
Model *yêu cầu*, code *thực thi*. Nhấn mạnh `tool_use_id`.

### Slide 7 — Structured output bằng tool
Tool làm "khuôn" JSON; ép `tool_choice`; đọc `input`, không chạy tool.

### Slide 8 — Lỗi thường gặp
Quên `tool_use_id`; sai `stop_reason`; quên đính lượt assistant.

### Slide 9 — Thẻ biện minh + Tóm tắt
Calculator: thay bằng gì / gỡ ra tụt gì. Bốn bước + structured output là nền cả khoá.

---

**Cheat sheet 1 dòng:** `create(tools=)` → nếu `stop_reason=="tool_use"`: chạy tool → gửi lại `{"type":"tool_result","tool_use_id":...}`.
