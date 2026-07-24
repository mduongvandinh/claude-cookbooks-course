# Ca hỏng mở màn — Chunk cắt ngang

!!! danger "Bắt đầu bằng cái hỏng (quy tắc ②)"
    Một pipeline có bộ chunk cắt cứng theo số ký tự. Nhiều khối mã và bảng tham số bị **cắt làm đôi** — nửa đầu
    chứa tên tham số, nửa sau chứa giá trị mặc định và cảnh báo.

## Bối cảnh

```python
# Bộ chunk HỎNG: cắt cứng 512 ký tự, không quan tâm cấu trúc
def chunk_broken(text, size=512):
    return [text[i:i+size] for i in range(0, len(text), size)]
```

Với tài liệu kỹ thuật, hàm này cắt ngang `def connect(host, port, timeout=30, retries=3):` — nửa đầu chunk có
tên tham số, nửa sau (chunk kế) có giá trị mặc định và ghi chú.

## Bài phá trước

<div class="predict" markdown>
**Dự đoán:** Chỉ số nào tụt trước — `recall@10` hay độ trung thành của câu trả lời? Vì sao?

<textarea class="predict-input" placeholder="Viết dự đoán của bạn — dài ít nhất một câu..."></textarea>
<button class="predict-btn">Khoá dự đoán & xem kết quả</button>

<div class="predict-result" hidden markdown>
`recall@10` **gần như không nhúc nhích**. Chunk nửa đầu vẫn chứa tên tham số nên vẫn khớp truy vấn và vẫn được
lấy về — theo mọi thước đo truy hồi, hệ thống vẫn "đúng".

Cái sụp là **độ trung thành**: mô hình nhận được nửa định nghĩa, và nó điền nốt nửa còn lại bằng cách **bịa**.
Lớp lỗi nguy hiểm nhất của RAG sinh ra ở đây — sai mà vẫn có trích dẫn.

**Bài học:** `recall@k` là chỉ số biết nói dối khi chunk không tự đủ nghĩa. Luôn ghép nó với một chỉ số đo ở
**đầu ra**, không bao giờ dùng một mình. (Bản sửa: chunking theo cấu trúc — buổi 1.2.)
</div>
</div>

## Vì sao đây là cách vào bài

Trục này đầy kỹ thuật hào nhoáng (rerank, HyDE...). Nhưng nếu **chunking còn hỏng**, mọi kỹ thuật xếp hạng tinh
vi đều vô nghĩa. Ca hỏng này ép bạn thấy: đo sai chỗ thì cải tiến sai chỗ. Ghi vào [sổ lỗi](../so-loi-test-case.md):
"recall@k một mình khi chunk không tự đủ nghĩa".

→ Tiếp: [1.1 — Đường cơ sở và chẩn đoán](1.1-duong-co-so/bai-giang.md)
