# 0.1 — Phân tích lỗi trước khi nghĩ tới chỉ số

!!! abstract "Mục tiêu"
    - Đọc tay 100 lượt tương tác thật, mã hoá mở thành 6–8 nhóm lỗi.
    - Ra được một danh sách nhóm lỗi có tần suất, xếp theo ảnh hưởng.
    - Chốt corpus riêng + action layer, giữ tới hết khoá.

## Vì sao đọc tay trước

Bản năng của kỹ sư là dựng dashboard ngay. Nhưng bạn không biết **đo cái gì** cho tới khi thấy lỗi thật trông
thế nào. Viết rubric trước khi đọc dữ liệu là đoán. Buổi này đảo lại: **đọc trước, đo sau**.

<div class="predict" markdown>
**Dự đoán:** Bạn đọc tay 100 lượt tương tác thật của một hệ thống. Dự đoán bạn sẽ rút ra được bao nhiêu *loại*
lỗi khác nhau?

<textarea class="predict-input" placeholder="Viết dự đoán của bạn — dài ít nhất một câu..."></textarea>
<button class="predict-btn">Mở kết quả</button>

<div class="predict-result" hidden markdown>
Gần như luôn rơi vào khoảng **6–8 nhóm**, dù bắt đầu từ 100 lỗi rời rạc. Ít hơn thì bạn gom quá thô; nhiều hơn
thì bạn chưa gom. Con số 6–8 không phải phép màu — nó phản ánh việc phần lớn lỗi của một hệ thống tụ về một số
ít nguyên nhân gốc.
</div>
</div>

## Quy trình mã hoá mở (open coding)

1. **Lấy mẫu 100 lượt thật** — không công cụ, không dashboard, chỉ một bảng tính. Mỗi dòng một lượt.
2. **Gán nhãn tự do** — với mỗi lượt sai, viết một cụm từ mô tả lỗi *bằng lời của bạn* (chưa cần phân loại).
3. **Gom nhóm** — sau khi gán hết, gom các cụm từ giống nhau lại thành 6–8 nhóm.
4. **Đếm tần suất** — mỗi nhóm bao nhiêu lượt.
5. **Xếp theo ảnh hưởng** — tần suất × mức nghiêm trọng, không chỉ tần suất.

**Kết quả bắt buộc:** một danh sách nhóm lỗi có tần suất, xếp theo ảnh hưởng. Đây là đầu vào cho bộ đề vàng
(buổi 0.2) — sáu loại câu hỏi phải bám các nhóm lỗi *có thật* này.

## Chốt corpus + action layer

Ngay buổi này, mỗi học viên chốt **corpus riêng**: kho tài liệu kỹ thuật của một sản phẩm (API docs, release
notes, bảng mã lỗi, config, migration guide). Kèm **action layer** — vài mock tool (tra bản ghi, cập nhật trạng
thái, mở ticket) để trục 03 sau này có action surface. Giữ nguyên tới hết khoá; đổi giữa chừng = chạy lại toàn
bộ đường cơ sở.

<div class="tool-justify" markdown>
**Thẻ biện minh — bảng tính (thay vì công cụ eval)**

- **Thay bằng gì vẫn chạy?** Một nền eval có sẵn.
- **Gỡ ra thì chỉ số nào tụt?** Không tụt gì — nhưng ở buổi đầu, công cụ che mất việc *đọc dữ liệu thật*. Dùng
  bảng tính có chủ ý để ép nhìn từng lượt.
</div>

## Lỗi thường gặp

- Nhảy sang đo chỉ số khi chưa đọc đủ dữ liệu → rubric bám lỗi tưởng tượng.
- Gom nhóm quá sớm (áp phân loại có sẵn) → bỏ sót nhóm lỗi đặc thù của hệ mình.
- Xếp hạng chỉ theo tần suất → bỏ qua lỗi hiếm nhưng nghiêm trọng.

## Tóm tắt

Đọc tay 100 lượt → 6–8 nhóm lỗi có tần suất → xếp theo ảnh hưởng. Đây là nền cho mọi thứ đo được sau này.

→ Tiếp: [0.2 — Bộ đề vàng và sáu loại câu hỏi](../0.2-bo-de-vang/bai-giang.md)

---

**Tài liệu buổi này:** [Instructor notes](instructor-notes.md) · [Bài tập](bai-tap.md) · [Lời giải](loi-giai.md) · [Slide outline](slide-outline.md)
