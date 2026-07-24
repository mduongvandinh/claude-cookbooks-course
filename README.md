# Claude Cookbooks Course — Giáo trình 5 trục

Bootcamp 10 tuần xây ứng dụng LLM sản xuất, tổ chức theo **5 trục vấn đề, eval-first**, xây từ bộ
[Claude Cookbooks](https://github.com/anthropics/claude-cookbooks) chính thức của Anthropic.

- **Trang syllabus (bản đồ khoá):** `docs/syllabus.html`
- **Nội dung bài (site tương tác):** MkDocs Material → `mkdocs serve`
- **Site:** https://mduongvandinh.github.io/claude-cookbooks-course/

## Bốn quy tắc sư phạm

1. **Dự đoán trước, chạy sau** — viết dự đoán rồi mới xem kết quả.
2. **Bắt đầu bằng cái hỏng** — mỗi trục mở màn bằng một pipeline lỗi cần sửa.
3. **Bánh cóc** — mọi câu hỏi/lỗi thành tài liệu vĩnh viễn, chỉ thêm không xoá.
4. **Vấn đề trước, công cụ sau** — mỗi công cụ phải qua "thẻ biện minh".

## Năm trục

| Trục | Câu hỏi trung tâm |
|---|---|
| 0 · Nền tảng (on-ramp) | Gọi API, prompt, structured output, một vòng tool use |
| 00 · Đo lường | Làm sao biết hệ thống tốt lên hay xấu đi mà không phải cảm tính? |
| 01 · Truy hồi | Tại sao nó lấy sai tài liệu — và là lỗi truy hồi hay lỗi sinh? |
| 02 · Sinh | Context đã đúng, vì sao vẫn bịa? |
| 03 · Vòng lặp | Khi nào cần agent thay vì pipeline tất định? |
| 04 · Vận hành | Nó hỏng thế nào lúc 2 giờ sáng? |

## Chạy cục bộ

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```

## Trạng thái

- [x] On-ramp Buổi 0
- [x] Trục 00 — Đo lường
- [x] Trục 01 — Truy hồi
- [x] Trục 02 — Sinh
- [x] Trục 03 — Vòng lặp
- [x] Trục 04 — Vận hành

Toàn bộ 5 trục + on-ramp đã có nội dung đầy đủ (mỗi buổi 5 file: bài giảng, instructor notes, bài tập, lời giải, slide).

Tài liệu thiết kế: `docs/planning/`.
