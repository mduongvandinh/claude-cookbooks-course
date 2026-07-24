# 2.3 — Từ chối trả lời (buổi khó nhất)

!!! abstract "Mục tiêu"
    - Dạy hệ thống nói "không có trong tài liệu" mà không thành cỗ máy từ chối.
    - Đo **từ chối đúng** và **từ chối nhầm** cùng nhau.
    - Thấy nhóm câu ngoài phạm vi (buổi 0.2) phát huy tác dụng.

## Hai chỉ số kéo nhau

<div class="predict" markdown>
**Dự đoán:** Bạn thêm câu "nếu không có trong tài liệu, hãy nói không biết" vào prompt. Dự đoán: điều gì xảy ra
với tỉ lệ **từ chối nhầm** (từ chối câu thực ra trả lời được)?

<textarea class="predict-input" placeholder="Viết dự đoán của bạn — dài ít nhất một câu..."></textarea>
<button class="predict-btn">Mở kết quả</button>

<div class="predict-result" hidden markdown>
**Từ chối nhầm tăng.** Đẩy mô hình từ chối mạnh hơn để giảm bịa (từ chối đúng tăng) gần như luôn kéo theo nó từ
chối cả những câu thực ra trả lời được (từ chối nhầm tăng). Hai chỉ số **kéo nhau** — không thể tối ưu một cái
mà bỏ cái kia. Phải báo cáo cả hai (đúng yêu cầu Cổng 02) và tìm điểm cân bằng.
</div>
</div>

## Prompt grounding — "Not specified"

Kỹ thuật từ notebook summarization: thay vì để mô hình bịa, hướng nó đánh dấu thiếu thông tin:

```python
system = (
    "Chỉ trả lời dựa trên tài liệu được cung cấp. "
    "Nếu thông tin không được nêu rõ trong tài liệu, hãy trả lời 'Không có trong tài liệu' — không suy đoán."
)
```

Kết hợp Citations API (buổi 2.1): nếu không có trích dẫn hợp lệ nào → tín hiệu để từ chối.

## Nhóm câu ngoài phạm vi (từ 0.2) phát huy tác dụng

Đây là chỗ nhóm **ngoài phạm vi** trong bộ đề vàng (buổi 0.2) thật sự cần thiết: nó đo **từ chối đúng**. Không có
nhóm này, bạn không bao giờ biết hệ thống có biết nói "không" hay không — nó chỉ toàn trả lời (và bịa).

<div class="tool-justify" markdown>
**Thẻ biện minh — prompt grounding "Không có trong tài liệu"**

- **Thay bằng gì vẫn chạy?** Để mô hình luôn cố trả lời.
- **Gỡ ra thì chỉ số nào tụt?** Từ chối đúng trên câu ngoài phạm vi — nhưng phải canh từ chối nhầm không vọt.
</div>

## Lỗi thường gặp

- Chỉ tối ưu từ chối đúng → từ chối nhầm vọt, hệ thành cỗ máy từ chối.
- Không có nhóm ngoài phạm vi để đo từ chối đúng.
- Từ chối bằng prompt mà không dùng tín hiệu trích dẫn.

## Tóm tắt

Dạy từ chối bằng grounding prompt + tín hiệu trích dẫn; đo từ chối đúng và nhầm cùng nhau; nhóm ngoài phạm vi là
thước đo. Đây là buổi khó nhất — cân bằng, không cực đoan.

→ Tiếp: [Cổng 02](../cong-02.md)
