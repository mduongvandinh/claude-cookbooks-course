# Ca hỏng mở màn — Ngữ cảnh cám dỗ

!!! danger "Bắt đầu bằng cái hỏng (quy tắc ②)"
    Truy hồi đã đúng — chunk chứa câu trả lời đúng *có* trong ngữ cảnh. Nhưng câu trả lời sinh ra vẫn sai.

## Bối cảnh

Bạn nạp vào ngữ cảnh bốn chunk:

- **Một chunk đúng** nhưng viết cụt lủn, khô khan.
- **Ba chunk sai** — nói về một phiên bản cũ — nhưng viết mạch lạc, dài hơn, có ví dụ đầy đủ.

Chunk đúng ở vị trí thứ ba trong bốn.

## Bài phá trước

<div class="predict" markdown>
**Dự đoán:** Mô hình sẽ dựa vào chunk nào? Và nếu bạn chuyển chunk đúng lên vị trí đầu tiên thì thay đổi bao nhiêu?

<textarea class="predict-input" placeholder="Viết dự đoán của bạn — dài ít nhất một câu..."></textarea>
<button class="predict-btn">Khoá dự đoán & xem kết quả</button>

<div class="predict-result" hidden markdown>
Mô hình **nghiêng mạnh về nhóm chunk trôi chảy và dài hơn** — độ mạch lạc của văn bản bị nhầm thành độ đáng tin.
Câu trả lời vẫn có trích dẫn, vẫn trung thành với *một* nguồn trong ngữ cảnh, và vẫn sai.

Dời chunk đúng lên đầu thường **cải thiện rõ rệt** — đó chính là hiệu ứng vị trí. Hai quan sát gộp lại cho một
kết luận khó chịu: **thứ tự chunk là một siêu tham số**, và hầu hết mọi người không bao giờ đo nó.

**Bài học:** trung thành với ngữ cảnh ≠ đúng. Nếu ngữ cảnh chứa sẵn thứ sai, phần sinh chỉ làm cái sai thuyết
phục hơn. → Đo bằng cách dịch chuyển vị trí (buổi 2.2).
</div>
</div>

## Vì sao đây là cách vào bài

Trục 01 lo *lấy đúng tài liệu*. Trục 02 lo *dùng đúng tài liệu đã lấy*. Ca hỏng này cho thấy: lấy đúng chưa đủ —
mô hình có thể phớt lờ chunk đúng vì nó kém hấp dẫn. Ghi vào [sổ lỗi](../so-loi-test-case.md): "nhầm mạch lạc
thành đáng tin".

→ Tiếp: [2.1 — Tách hai loại lỗi](2.1-tach-loi/bai-giang.md)
