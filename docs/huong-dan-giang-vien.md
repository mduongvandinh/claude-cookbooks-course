# Hướng dẫn giảng viên

Tài liệu này dành cho bạn — người đứng lớp. Nó giải thích cơ chế vận hành của khoá học, không phải nội dung
kỹ thuật. Đọc kỹ trước buổi đầu tiên.

## Bốn quy tắc sư phạm (bắt buộc mọi buổi)

Đây là phần khiến giáo trình này khác một playlist notebook. Bỏ bốn quy tắc, phần còn lại chỉ là mục lục.

### ① Dự đoán trước, chạy sau
**Vì sao:** người không dự đoán thì không học được gì từ kết quả — họ chỉ xác nhận thứ vừa nhìn thấy.
**Cách áp:** trước mỗi thí nghiệm, học viên viết dự đoán ra và khoá lại; chỉ khi đã khoá mới xem kết quả.
Trong tài liệu, widget dự đoán khoá ô kết quả tới khi học viên gõ ít nhất một câu.

### ② Bắt đầu bằng cái hỏng
**Vì sao:** chữa một hệ thống hỏng dạy được nhiều gấp bội việc gõ lại một hệ thống đúng, và nó rèn đúng kỹ
năng người dạy cần — đoán được học viên sẽ kẹt ở đâu.
**Cách áp:** mỗi trục mở màn bằng một pipeline đã cấy lỗi (bài phá trước), không phải sample chạy đúng.

### ③ Bánh cóc — chỉ quay một chiều
**Vì sao:** kiến thức người dạy phải tích luỹ một chiều, không rơi rụng.
**Cách áp:** mọi câu hỏi bạn trả lời chưa trôi khi thử giảng đều rơi vào [bộ câu hỏi vàng](truc-00-do-luong/bo-cau-hoi-vang.md)
và ở lại đó tới khi có câu trả lời viết ra. Với học viên: mọi lỗi từng gặp thành một
[test case](so-loi-test-case.md) vĩnh viễn, không được xoá.

### ④ Vấn đề trước, công cụ sau
**Vì sao:** dạy sản phẩm thì lỗi thời; dạy nguyên lý thì bền.
**Cách áp:** không buổi nào mang tên một sản phẩm. Mỗi lần giới thiệu một công cụ, bài giảng phải có
**"thẻ biện minh"**: thay bằng gì vẫn chạy? gỡ ra thì chỉ số nào tụt? Không qua thẻ này thì cắt.

## Cấu trúc mỗi buổi (5 file)

| File | Dùng khi nào |
|---|---|
| `bai-giang.md` | Nội dung chính — đọc/giảng trên lớp, có bài phá trước và thẻ biện minh |
| `instructor-notes.md` | Chuẩn bị của bạn — thời lượng, thông điệp chốt, câu hỏi gợi mở, điểm hay vấp |
| `bai-tap.md` | Giao cho học viên — bài phân bậc Core/Đi sâu + bước hướng tới cổng |
| `loi-giai.md` | Đáp án + rubric chấm |
| `slide-outline.md` | Khung slide + cheat sheet 1 trang |

## Cơ chế cổng (phân tầng)

Chấm học viên **bằng cổng**, không bằng bài nộp cuối khoá. Mỗi cổng có tiêu chí bằng số. Cổng **phân tầng**:

- **Ngưỡng tối thiểu để đi tiếp** — đủ vượt cổng, sang trục sau.
- **Ngưỡng đạt chuẩn** — mức "Vững".
- Học viên chưa đạt tối thiểu → **buổi remediation**, không bị bỏ lại nhưng không qua cổng.

Ba mức tổng kết: **Đạt** (5/5 cổng) → **Vững** (5/5 + vấn đáp) → **Dạy được** (+ chữa pipeline hỏng của người
khác trong 30 phút).

**Bài thi cuối "đổi máy":** hai học viên đổi repo, mỗi người 30 phút tìm và mô tả 3 điểm yếu lớn nhất của hệ
thống người kia, kèm số đo. Bài này đo đúng thứ cả khoá hướng tới: chẩn đoán một hệ thống chưa từng thấy.

## Checklist chuẩn bị trước mỗi buổi

- [ ] Đạt **28/30** [câu hỏi vàng](truc-00-do-luong/bo-cau-hoi-vang.md) trước buổi dạy chính thức đầu tiên.
- [ ] Đọc `instructor-notes.md` của buổi.
- [ ] Chạy thử notebook nguồn trên Colab (đặt `ANTHROPIC_API_KEY`).
- [ ] Chốt **corpus + action layer** cùng lớp ở buổi 0.1 và giữ nguyên tới hết khoá.
- [ ] Mở sẵn [sổ lỗi](so-loi-test-case.md) để ghi lỗi mới phát sinh trong buổi.
