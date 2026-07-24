# 1.4 — Xếp hạng lại và bài toán ngân sách

!!! abstract "Mục tiêu"
    - Chuyển từ **độ bao phủ** sang **độ chính xác** bằng xếp hạng lại.
    - Đo cả điểm chất lượng lẫn độ trễ trong cùng một lần chạy.
    - Lập bảng đóng góp: mỗi kỹ thuật thêm bao nhiêu điểm, tốn bao nhiêu ms.

## Xếp hạng lại — từ bao phủ sang chính xác

Kỹ thuật #6: lấy rộng (top-20 → top-50) để **bao phủ**, rồi xếp hạng lại để lấy **chính xác** top-k. Hai cách:

**Reranker bằng Claude** (từ RAG guide — chú ý prefill + stop_sequences):

```python
prompt = f"""Query: {query}
Bạn sẽ nhận một nhóm tài liệu, hãy chọn đúng {k} tài liệu liên quan nhất.
<documents>{joined_summaries}</documents>
Chỉ xuất chỉ số của {k} tài liệu, phân tách bằng dấu phẩy, trong <relevant_indices></relevant_indices>."""
response = client.messages.create(
    model="claude-haiku-4-5", max_tokens=50, temperature=0,
    messages=[{"role": "user", "content": prompt},
              {"role": "assistant", "content": "<relevant_indices>"}],   # prefill
    stop_sequences=["</relevant_indices>"])
```
Kết quả điển hình: accuracy 78% → 85%.

**Reranker chuyên dụng (Cohere)** — nhanh hơn, từ contextual-embeddings:

```python
import cohere
co = cohere.Client()
res = co.rerank(model="rerank-english-v3.0", query=query, documents=documents, top_n=k)
```

## Bài toán ngân sách — chất lượng vs độ trễ

<div class="predict" markdown>
**Dự đoán:** Bật rerank tăng accuracy 78% → 85% nhưng thêm một lượt gọi model mỗi truy vấn. Dự đoán: chi phí
này có đáng không, và bạn cần đo gì để quyết?

<textarea class="predict-input" placeholder="Viết dự đoán của bạn — dài ít nhất một câu..."></textarea>
<button class="predict-btn">Mở kết quả</button>

<div class="predict-result" hidden markdown>
Chưa quyết được nếu chỉ nhìn accuracy. Đây là **buổi đầu tiên** chất lượng và độ trễ xuất hiện cạnh nhau — đúng
tinh thần Trục 04. Cần đo **độ trễ thêm (ms)** và **chi phí thêm** của rerank, rồi so với mức tăng 7 điểm. Với
reranker Cohere (nhanh) đánh đổi khác với reranker bằng Claude (chậm hơn, đắt hơn). Câu trả lời nằm ở bảng đóng
góp, không ở một con số accuracy.
</div>
</div>

**Bảng đóng góp** (yêu cầu của Cổng 01): mỗi kỹ thuật bật thêm ghi (điểm thêm | ms thêm), đo trước/sau.

| Kỹ thuật | Điểm thêm | ms thêm |
|---|---|---|
| Hybrid BM25 | +4 | +15 |
| Contextual retrieval | +5 | 0 (đã ingest) |
| Rerank (Claude) | +7 | +800 |
| Rerank (Cohere) | +6 | +120 |

<div class="tool-justify" markdown>
**Thẻ biện minh — xếp hạng lại**

- **Thay bằng gì vẫn chạy?** Lấy top-k trực tiếp từ tìm kiếm.
- **Gỡ ra thì chỉ số nào tụt?** Độ chính xác top-5 khi tài liệu đúng nằm trong top-50 nhưng trượt top-5 — trả
  giá bằng độ trễ/chi phí một lượt gọi.
</div>

## Lỗi thường gặp

- Bật rerank mà không đo độ trễ thêm.
- Dùng reranker Claude khi Cohere đủ (đắt/chậm hơn).
- Không lập bảng đóng góp → không biết kỹ thuật nào thật sự có tác dụng.

## Tóm tắt

Lấy rộng để bao phủ, rerank để chính xác; đo chất lượng **và** độ trễ cùng lúc; lập bảng đóng góp. Đây là cửa
ngõ sang tư duy vận hành (Trục 04).

→ Tiếp: [Cổng 01](../cong-01.md)

---

**Tài liệu buổi này:** [Instructor notes](instructor-notes.md) · [Bài tập](bai-tap.md) · [Lời giải](loi-giai.md) · [Slide outline](slide-outline.md)
