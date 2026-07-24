# Ca hỏng mở màn — Công cụ mô tả tồi

!!! danger "Bắt đầu bằng cái hỏng (quy tắc ②)"
    Một agent chọn sai công cụ. Bản năng là đổi mô hình mạnh hơn. Nhưng lỗi có thể không nằm ở mô hình.

## Bối cảnh

Agent có ba công cụ, mô tả lần lượt là `search`, `lookup`, `find`. Độ chính xác chọn công cụ đo được là **0.55**.
Học viên đề nghị đổi sang mô hình mạnh hơn và đắt hơn.

```python
tools = [
    {"name": "search", "description": "search", "input_schema": {...}},
    {"name": "lookup", "description": "lookup", "input_schema": {...}},
    {"name": "find",   "description": "find",   "input_schema": {...}},
]
```

## Bài phá trước

<div class="predict" markdown>
**Dự đoán:** Đổi mô hình sẽ cải thiện được bao nhiêu, so với việc chỉ viết lại ba dòng mô tả công cụ?

<textarea class="predict-input" placeholder="Viết dự đoán của bạn — dài ít nhất một câu..."></textarea>
<button class="predict-btn">Khoá dự đoán & xem kết quả</button>

<div class="predict-result" hidden markdown>
Đổi mô hình thường **nhích được vài điểm**. Viết lại mô tả công cụ — nêu rõ công cụ đó tìm gì, trong phạm vi
nào, trả về gì, và khi nào *không* nên dùng — thường **nhảy vọt hơn hẳn, với chi phí bằng không**.

Ba công cụ `search`/`lookup`/`find` gần như đồng nghĩa với mô hình — nó không có cơ sở để chọn. Mô tả tốt:
"`search_docs`: tìm trong tài liệu API theo từ khoá, trả về đoạn văn; dùng cho câu hỏi 'cách dùng'. Không dùng
cho tra cứu bản ghi khách hàng."

**Bài học:** phần lớn cái mà nhóm phát triển gọi là "mô hình chưa đủ giỏi" thật ra là **khung chạy chưa đủ tốt**.
</div>
</div>

## Vì sao đây là cách vào bài

Trục này đầy cám dỗ "nâng cấp mô hình". Ca hỏng ép bạn thấy: trước khi đổ tiền vào mô hình mạnh hơn, hãy chứng
minh khung chạy đã hết dư địa — gần như chưa bao giờ hết. Ghi vào [sổ lỗi](../so-loi-test-case.md): "đổ lỗi mô
hình khi mô tả công cụ mơ hồ".

→ Tiếp: [3.1 — Khi nào không cần agent](3.1-khi-nao-khong-agent/bai-giang.md)
