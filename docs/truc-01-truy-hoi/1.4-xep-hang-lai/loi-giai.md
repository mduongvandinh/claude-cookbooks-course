# Lời giải — Buổi 1.4

## Core — Rerank
```python
# Reranker Claude (prefill + stop_sequences) — xem bài giảng; hoặc Cohere:
import cohere
co = cohere.Client()
top5 = co.rerank(model="rerank-english-v3.0", query=q, documents=docs, top_n=5)
```
**Rubric:** hai cặp (accuracy, ms) trước/sau (3đ).

## Đi sâu — Bảng đóng góp
| Kỹ thuật | Điểm thêm | ms thêm |
|---|---|---|
| Hybrid | +4 | +15 |
| Contextual | +5 | 0 |
| Rerank Cohere | +6 | +120 |
| Rerank Claude | +7 | +800 |

**Rubric:** bảng đủ (2đ); kết luận theo điểm/ms (1đ).

## Capstone — Cổng 01
**Rubric:** recall@10 +≥8 (2đ); bảng đóng góp đầy đủ (1đ); nêu 1 kỹ thuật làm tệ đi (1đ).
