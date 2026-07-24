# Ca hỏng mở màn — Đánh đổi

!!! danger "Bắt đầu bằng cái hỏng (quy tắc ②)"
    Trục này mở màn bằng một **quyết định hỏng** — một câu trả lời nghe có vẻ hợp lý nhưng thiếu dữ liệu để đúng.

## Bối cảnh

Bạn bật xếp hạng lại (rerank): điểm chất lượng **tăng 6 điểm** trên bộ đề vàng. Cùng lúc, `p99` **tăng gấp bốn**
và chi phí mỗi truy vấn **tăng khoảng 40%**.

## Bài phá trước

<div class="predict" markdown>
**Dự đoán:** Giữ hay bỏ? Và bạn cần thêm những số liệu nào mới quyết được?

<textarea class="predict-input" placeholder="Viết dự đoán của bạn — dài ít nhất một câu..."></textarea>
<button class="predict-btn">Khoá dự đoán & xem kết quả</button>

<div class="predict-result" hidden markdown>
**Không có đáp án đúng nếu chỉ nhìn hai con số.** Câu trả lời tốt phải hỏi ngược lại:

- Ngưỡng độ trễ mà người dùng bỏ đi là bao nhiêu? `p99` gấp bốn có vượt ngưỡng đó không?
- 6 điểm đó rơi vào **nhóm truy vấn nào** — nhóm chiếm 2% lưu lượng hay 40%?
- Có bật rerank **theo điều kiện** được không (chỉ khi điểm truy hồi thấp)?

Học viên nào trả lời ngay "giữ" hoặc "bỏ" là chưa qua trục này. **Kỹ năng cần dạy là nhận ra dữ liệu còn
thiếu**, không phải chọn nhanh.

**Bài học:** mọi quyết định vận hành là bài toán **ba chiều** — chất lượng, độ trễ, chi phí. Ai chỉ báo cáo
một chiều là đang giấu hai chiều còn lại.
</div>
</div>

## Vì sao đây là cách vào bài

Trục 00–03 dạy làm hệ thống *tốt hơn*. Trục 04 dạy quyết định *có nên áp dụng cái tốt hơn đó không* — vì mỗi
cải tiến đều có giá bằng độ trễ và tiền. Ghi lỗi này vào [sổ lỗi](../so-loi-test-case.md): "báo cáo một chiều".

→ Tiếp: [4.1 — Nhìn thấy được thì mới sửa được](4.1-vet-chay/bai-giang.md)
