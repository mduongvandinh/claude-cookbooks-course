# 1.1 — Đường cơ sở và chẩn đoán

[:material-notebook: Mở retrieval_augmented_generation trên Colab](https://colab.research.google.com/github/anthropics/claude-cookbooks/blob/main/capabilities/retrieval_augmented_generation/guide.ipynb){ .md-button }

!!! abstract "Mục tiêu"
    - Dựng đường cơ sở **tệ có chủ ý** để có mốc so sánh.
    - Đo `recall@k` ở nhiều k, đọc đường cong chứ không đọc một con số.
    - Dùng cây chẩn đoán để định vị lỗi truy hồi.

## Vì sao baseline phải tệ có chủ ý

Không có mốc thì không đo được cải tiến. Baseline: chunk cố định, embedding thuần (`voyage-2`), không lọc, không
rerank. Mọi kỹ thuật sau này phải chứng minh nó **đánh bại** baseline này bằng số.

```python
import voyageai, numpy as np
vo = voyageai.Client()

def embed(texts, model="voyage-2", batch=128):
    out = []
    for i in range(0, len(texts), batch):
        out += vo.embed(texts[i:i+batch], model=model).embeddings
    return np.array(out)

# Index: nhúng toàn bộ chunk một lần
chunk_vecs = embed([c["text"] for c in chunks])

def search(query, k=3):
    q = embed([query])[0]
    sims = chunk_vecs @ q                       # dot-product
    idx = np.argsort(sims)[::-1][:k]
    return [chunks[i] for i in idx]
```

## Đo recall@k — đọc đường cong

<div class="predict" markdown>
**Dự đoán:** Bạn đo recall ở k = 1, 3, 5, 10, 20. Dự đoán đường cong recall@k có hình gì, và điểm nào đáng chú ý nhất?

<textarea class="predict-input" placeholder="Viết dự đoán của bạn — dài ít nhất một câu..."></textarea>
<button class="predict-btn">Mở kết quả</button>

<div class="predict-result" hidden markdown>
Đường cong **tăng dần và bão hoà**. Điểm đáng chú ý: khoảng cách giữa recall@5 và recall@20 — nếu tài liệu đúng
*có* trong top-20 nhưng *không* trong top-5, thì vấn đề là **xếp hạng** (buổi 1.4), không phải index. Nếu
recall@20 vẫn thấp, tài liệu đúng không được lấy về — vấn đề ở **chunking/embedding** (buổi 1.2). Một con số
recall@10 đơn lẻ không cho bạn biết điều này; cả đường cong mới cho.
</div>
</div>

```python
def recall_at_k(retrieved_links, correct_links):
    tp = len(set(retrieved_links) & set(correct_links))
    return tp / len(correct_links)
# Precision, F1, MRR@k đo tương tự (MRR = 1/hạng của hit đầu tiên).
```

## Cây chẩn đoán

Khi truy hồi sai, hỏi theo thứ tự:

1. **Tài liệu đúng có trong index không?** — không → lỗi chunking/ingest.
2. **Có trong index nhưng không được lấy?** — recall@20 thấp → lỗi embedding/truy vấn.
3. **Được lấy nhưng xếp hạng thấp?** — có trong top-50 mà trượt top-5 → lỗi xếp hạng (rerank).

<div class="tool-justify" markdown>
**Thẻ biện minh — embedding (voyage-2)**

- **Thay bằng gì vẫn chạy?** BM25/keyword thuần.
- **Gỡ ra thì chỉ số nào tụt?** Recall trên câu hỏi diễn đạt khác tài liệu (ngữ nghĩa) — nhưng embedding thua ở
  mã lỗi/tên hàm (buổi 1.3).
</div>

## Lỗi thường gặp

- Đọc một con số recall@10 thay vì cả đường cong.
- Không có baseline → không đo được cải tiến.
- Nhầm lỗi xếp hạng với lỗi index.

## Tóm tắt

Baseline tệ có chủ ý + đường cong recall@k + cây chẩn đoán ba nhánh. Chẩn đoán trước, tối ưu sau.

→ Tiếp: [1.2 — Chunking và siêu dữ liệu](../1.2-chunking-sieu-du-lieu/bai-giang.md)

---

**Tài liệu buổi này:** [Instructor notes](instructor-notes.md) · [Bài tập](bai-tap.md) · [Lời giải](loi-giai.md) · [Slide outline](slide-outline.md)
