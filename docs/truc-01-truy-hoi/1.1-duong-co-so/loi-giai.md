# Lời giải — Buổi 1.1

## Core — Baseline + recall@k
```python
import voyageai, numpy as np
vo = voyageai.Client()
def embed(texts, model="voyage-2", batch=128):
    out = []
    for i in range(0, len(texts), batch):
        out += vo.embed(texts[i:i+batch], model=model).embeddings
    return np.array(out)
chunk_vecs = embed([c["text"] for c in chunks])
def search(q, k=3):
    qv = embed([q])[0]; idx = np.argsort(chunk_vecs @ qv)[::-1][:k]
    return [chunks[i] for i in idx]
def recall_at_k(retrieved, correct):
    return len(set(retrieved) & set(correct)) / len(correct)
```
**Rubric:** đường cong recall@k tại 5 mốc (2đ); đối chiếu dự đoán (1đ).

## Đi sâu — Cây chẩn đoán
**Rubric:** 5 câu phân nhánh, mỗi câu có bằng chứng "có trong index / có trong top-20" (3đ).

## Capstone
**Rubric:** baseline chạy, recall@10 ghi làm mốc (2đ).
