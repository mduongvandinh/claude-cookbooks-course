# Giáo trình 5 trục

Một khoá bootcamp **10 tuần** dạy xây ứng dụng LLM sản xuất, tổ chức theo **trục vấn đề** thay vì trục
tài liệu, và **eval-first** — đo lường đi trước tất cả. Xây từ bộ
[Claude Cookbooks](https://github.com/anthropics/claude-cookbooks) chính thức của Anthropic.

Kho notebook chỉ là phụ tùng. Thứ quyết định là câu hỏi mà mỗi buổi phải trả lời, và cái **cổng bằng số**
mà học viên phải vượt trước khi được đi tiếp.

## Năm trục (và một on-ramp)

| Trục | Câu hỏi trung tâm |
|---|---|
| **0 · Nền tảng** | Gọi API, prompt, structured output, một vòng tool use (on-ramp cho người mới) |
| **00 · Đo lường** | Làm sao biết hệ thống tốt lên hay xấu đi mà không phải cảm tính? |
| **01 · Truy hồi** | Tại sao nó lấy sai tài liệu — và là lỗi truy hồi hay lỗi sinh? |
| **02 · Sinh** | Context đã đúng, vì sao vẫn bịa? |
| **03 · Vòng lặp** | Khi nào cần agent thay vì pipeline tất định? |
| **04 · Vận hành** | Nó hỏng thế nào lúc 2 giờ sáng? |

> Bản pilot hiện có: **On-ramp Buổi 0** và **Trục 00 — Đo lường**. Các trục còn lại đang triển khai theo cùng template.

**[→ Xem bản đồ 5 trục đầy đủ (syllabus)](syllabus.html)** — bốn quy tắc sư phạm, các cổng, lịch 10 tuần,
bộ câu hỏi vàng, và bài thi "đổi máy".

## Bốn quy tắc học tập

1. **Dự đoán trước, chạy sau** — viết dự đoán rồi mới xem kết quả.
2. **Bắt đầu bằng cái hỏng** — mỗi trục mở màn bằng một pipeline lỗi cần sửa.
3. **Bánh cóc** — mọi câu hỏi/lỗi thành tài liệu vĩnh viễn, chỉ thêm không xoá.
4. **Vấn đề trước, công cụ sau** — mỗi công cụ phải qua "thẻ biện minh".

Chi tiết trong [Hướng dẫn giảng viên](huong-dan-giang-vien.md).

## Bắt đầu

1. [Cài đặt môi trường](setup-moi-truong.md) — API key, SDK, chạy notebook.
2. [Buổi 0 — Nền tảng](on-ramp/index.md) — nếu bạn mới với Claude API.
3. [Trục 00 — Đo lường](truc-00-do-luong/index.md) — điểm khởi đầu thật sự của khoá.

## Thử ngay quy tắc ①

<div class="predict" markdown>
**Dự đoán:** Khi gọi Claude với một tool, `stop_reason` sẽ là gì nếu model quyết định dùng tool?

<textarea class="predict-input" placeholder="Viết dự đoán của bạn..."></textarea>
<button class="predict-btn">Mở kết quả</button>

<div class="predict-result" hidden markdown>
`stop_reason == "tool_use"`. Đây là tín hiệu để bạn chạy tool và gửi `tool_result` trở lại cho model.
</div>
</div>
