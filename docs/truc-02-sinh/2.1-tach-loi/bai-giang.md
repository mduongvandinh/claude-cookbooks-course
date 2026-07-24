# 2.1 — Tách hai loại lỗi

[:material-notebook: Mở using_citations trên Colab](https://colab.research.google.com/github/anthropics/claude-cookbooks/blob/main/misc/using_citations.ipynb){ .md-button }

!!! abstract "Mục tiêu"
    - Phân biệt **trung thành với ngữ cảnh** và **hữu ích với người hỏi**.
    - Đo trần của phần sinh bằng thí nghiệm cô lập.
    - Áp trích dẫn ở **cấp câu** bằng Citations API.

## Hai chỉ số khác nhau, có thể ngược chiều

<div class="predict" markdown>
**Dự đoán:** Một câu trả lời có thể **trung thành 100%** với tài liệu mà vẫn **vô dụng** với người hỏi không?
Cho một tình huống.

<textarea class="predict-input" placeholder="Viết dự đoán của bạn — dài ít nhất một câu..."></textarea>
<button class="predict-btn">Mở kết quả</button>

<div class="predict-result" hidden markdown>
**Có.** Ví dụ: người dùng hỏi "làm sao khắc phục lỗi X", tài liệu chỉ mô tả lỗi X mà không có cách khắc phục.
Câu trả lời "tài liệu mô tả lỗi X là..." trung thành tuyệt đối nhưng vô dụng. Hai chỉ số — **trung thành** và
**hữu ích** — tách biệt và đôi khi ngược chiều. Bạn phải đo riêng, và Cổng 02 chấm trung thành (vì bịa nguy hiểm
hơn vô dụng).
</div>
</div>

## Thí nghiệm cô lập — đo trần của phần sinh

Đưa context **hoàn hảo bằng tay** (không qua truy hồi), đo tỉ lệ bịa còn lại. Con số đó là **trần** của phần
sinh — mọi lỗi truy hồi đã bị loại. Nếu vẫn bịa nhiều, vấn đề nằm ở sinh, không ở truy hồi (đúng như ca hỏng).

## Trích dẫn cấp câu — Citations API

Thay vì "tin lời" mô hình, ép nó neo từng câu vào nguồn. Citations API tự chia tài liệu thành câu và trả về
trích dẫn có kiểm chứng:

```python
documents = [{
    "type": "document",
    "source": {"type": "text", "media_type": "text/plain", "data": body},
    "title": title,
    "citations": {"enabled": True},
}]
response = client.messages.create(
    model="claude-sonnet-5", max_tokens=1024,
    system="Trả lời ngắn gọn dựa trên tài liệu được cung cấp.",
    messages=[
        {"role": "user", "content": documents},
        {"role": "user", "content": [{"type": "text", "text": cau_hoi}]},
    ],
)

# Đọc trích dẫn: khối text có .citations
for block in response.content:
    if block.type == "text" and getattr(block, "citations", None):
        for c in block.citations:
            print(c.cited_text, "—", c.document_title)   # c.type: char_location/page_location/...
```

Ưu điểm (theo notebook): API **không** trả trích dẫn tới nguồn không được cung cấp — grounding do chính tính
năng đảm bảo, không phụ thuộc prompt.

<div class="tool-justify" markdown>
**Thẻ biện minh — Citations API**

- **Thay bằng gì vẫn chạy?** Prompt "hãy trích dẫn nguồn" (mô hình có thể bịa trích dẫn).
- **Gỡ ra thì chỉ số nào tụt?** Độ kiểm chứng của trích dẫn — API đảm bảo trích dẫn trỏ đúng nguồn có thật.
</div>

## Lỗi thường gặp

- Gộp trung thành và hữu ích làm một chỉ số.
- Không làm thí nghiệm cô lập → đổ lỗi truy hồi cho phần sinh.
- Tin trích dẫn do prompt sinh (có thể bịa) thay vì Citations API.

## Tóm tắt

Trung thành ≠ hữu ích; đo trần phần sinh bằng context hoàn hảo; trích dẫn cấp câu bằng Citations API (kiểm chứng được).

→ Tiếp: [2.2 — Ngữ cảnh dài, mâu thuẫn, và vị trí](../2.2-ngu-canh-dai/bai-giang.md)

---

**Tài liệu buổi này:** [Instructor notes](instructor-notes.md) · [Bài tập](bai-tap.md) · [Lời giải](loi-giai.md) · [Slide outline](slide-outline.md)
