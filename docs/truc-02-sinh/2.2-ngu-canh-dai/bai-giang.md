# 2.2 — Ngữ cảnh dài, mâu thuẫn, và vị trí

!!! abstract "Mục tiêu"
    - Đo hiện tượng **thông tin ở giữa ngữ cảnh bị bỏ sót**.
    - Xử lý hai tài liệu mâu thuẫn vì khác phiên bản.
    - Tìm điểm gãy: nhồi thêm chunk không phải lúc nào cũng tốt hơn.

## Lost-in-the-middle — đo bằng dịch vị trí

<div class="predict" markdown>
**Dự đoán:** Bạn đặt chunk chứa câu trả lời đúng lần lượt ở đầu, giữa, cuối một ngữ cảnh dài (20 chunk). Dự
đoán: tỉ lệ trả lời đúng theo vị trí có hình gì?

<textarea class="predict-input" placeholder="Viết dự đoán của bạn — dài ít nhất một câu..."></textarea>
<button class="predict-btn">Mở kết quả</button>

<div class="predict-result" hidden markdown>
Hình chữ **U**: cao ở đầu và cuối, **thấp ở giữa**. Thông tin nằm giữa ngữ cảnh dài dễ bị bỏ sót nhất. Đây là
lý do thứ tự chunk là siêu tham số — đặt chunk quan trọng ở đầu (hoặc cuối), đừng chôn ở giữa. Đo bằng cách dịch
vị trí chunk đúng và ghi tỉ lệ đúng theo từng vị trí.
</div>
</div>

## Mâu thuẫn phiên bản — phân xử trong prompt

Hai tài liệu nói ngược nhau vì khác phiên bản. Mô hình mặc định chọn *cái nào*? Không nên phó mặc — **quy tắc
phân xử phải nằm trong prompt và phải kiểm chứng được**:

```python
system = (
    "Khi các tài liệu mâu thuẫn, ưu tiên tài liệu có phiên bản mới hơn (trường 'version'). "
    "Nếu không xác định được phiên bản, nêu rõ có mâu thuẫn thay vì chọn bừa."
)
```

Kết hợp lọc metadata phiên bản ở Trục 01 (buổi 1.2) — chặn mâu thuẫn từ khâu truy hồi.

## Nhồi thêm chunk — tìm điểm gãy

Thêm chunk không phải lúc nào cũng tốt hơn: quá nhiều ngữ cảnh làm loãng, tăng lost-in-the-middle và chi phí.
Tìm điểm gãy bằng **thực nghiệm** — đo chất lượng theo số chunk (3, 5, 10, 20) và chọn điểm bão hoà.

<div class="tool-justify" markdown>
**Thẻ biện minh — quy tắc phân xử trong prompt**

- **Thay bằng gì vẫn chạy?** Để mô hình tự chọn.
- **Gỡ ra thì chỉ số nào tụt?** Tỉ lệ trả lời đúng phiên bản khi có mâu thuẫn — không kiểm soát được nếu phó mặc.
</div>

## Lỗi thường gặp

- Chôn chunk quan trọng ở giữa ngữ cảnh dài.
- Phó mặc mô hình chọn khi tài liệu mâu thuẫn.
- Nhồi càng nhiều chunk càng tốt (không đo điểm gãy).

## Tóm tắt

Đo lost-in-the-middle bằng dịch vị trí; phân xử mâu thuẫn bằng quy tắc trong prompt (kiểm chứng được); tìm điểm
gãy số chunk bằng thực nghiệm.

→ Tiếp: [2.3 — Từ chối trả lời](../2.3-tu-choi/bai-giang.md)
