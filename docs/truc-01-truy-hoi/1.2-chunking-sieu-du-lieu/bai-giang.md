# 1.2 — Chunking và siêu dữ liệu (hai đòn bẩy lớn nhất)

[:material-notebook: Mở contextual-embeddings trên Colab](https://colab.research.google.com/github/anthropics/claude-cookbooks/blob/main/capabilities/contextual-embeddings/guide.ipynb){ .md-button }

!!! abstract "Mục tiêu"
    - Chunk theo **cấu trúc tài liệu**, không theo số ký tự.
    - Hiểu vì sao "chunk bao nhiêu token" là câu hỏi sai.
    - Lọc cứng theo phiên bản/sản phẩm **trước** khi xếp hạng.

## Câu hỏi đúng không phải "bao nhiêu token"

<div class="predict" markdown>
**Dự đoán:** Hai bộ chunk cùng kích thước 512 token, một cắt theo ký tự, một cắt theo mục/tiểu mục. Dự đoán:
recall khác nhau nhiều không, và độ trung thành khác nhau nhiều không?

<textarea class="predict-input" placeholder="Viết dự đoán của bạn — dài ít nhất một câu..."></textarea>
<button class="predict-btn">Mở kết quả</button>

<div class="predict-result" hidden markdown>
Recall có thể **gần bằng nhau**, nhưng độ trung thành khác hẳn. Câu hỏi đúng không phải "chunk bao nhiêu token"
mà là **"chunk có tự đủ nghĩa không"**. Chunk theo cấu trúc giữ nguyên một định nghĩa/khối mã/bảng — mô hình
nhận đủ ngữ cảnh, không phải bịa nửa còn lại (đúng như ca hỏng mở màn).
</div>
</div>

Chunk theo cấu trúc: cắt ở ranh giới mục, tiểu mục, khối mã — không cắt ngang một đơn vị nghĩa.

## Bổ sung ngữ cảnh vào chunk (contextual retrieval)

Kỹ thuật #7: với mỗi chunk, cho Claude **toàn bộ tài liệu** (cache lại) + chunk, xin một câu ngữ cảnh ngắn, rồi
**gắn trước chunk trước khi nhúng**:

```python
CHUNK_CONTEXT_PROMPT = """
Đây là chunk cần đặt vào ngữ cảnh của cả tài liệu:
<chunk>{chunk_content}</chunk>
Hãy cho một câu ngữ cảnh ngắn gọn để định vị chunk này trong tài liệu, phục vụ tìm kiếm.
Chỉ trả lời câu ngữ cảnh, không gì khác.
"""
# Gọi claude-haiku-4-5, cache_control cho phần tài liệu (đọc ~70-80% từ cache)
text_to_embed = f"{contextualized_text}\n\n{chunk['content']}"
```

Kết quả điển hình (từ notebook): Pass@10 baseline 87% → contextual embeddings 92%.

## Lọc theo siêu dữ liệu

Kỹ thuật #3: gắn phiên bản, sản phẩm, ngày vào metadata; **lọc cứng** trước khi tìm ngữ nghĩa. Đây là cách chữa
lỗi "đúng nội dung nhưng sai phiên bản" — một trong sáu loại câu hỏi ở Trục 00.

<div class="tool-justify" markdown>
**Thẻ biện minh — contextual retrieval**

- **Thay bằng gì vẫn chạy?** Nhúng chunk trần.
- **Gỡ ra thì chỉ số nào tụt?** Pass@k cho chunk phụ thuộc ngữ cảnh — trả giá bằng chi phí sinh ngữ cảnh (giảm
  nhờ prompt caching).
</div>

## Lỗi thường gặp

- Cắt theo số ký tự → chunk vỡ nghĩa (ca hỏng).
- Bỏ metadata → trả sai phiên bản.
- Sinh ngữ cảnh mà không cache → chi phí ingest tăng vọt.

## Tóm tắt

Chunk theo cấu trúc + gắn ngữ cảnh + lọc metadata cứng. Đây là hai đòn bẩy lớn nhất, tối ưu chúng trước rerank.

→ Tiếp: [1.3 — Lai ghép, viết lại truy vấn, HyDE](../1.3-lai-ghep-hyde/bai-giang.md)

---

**Tài liệu buổi này:** [Instructor notes](instructor-notes.md) · [Bài tập](bai-tap.md) · [Lời giải](loi-giai.md) · [Slide outline](slide-outline.md)
