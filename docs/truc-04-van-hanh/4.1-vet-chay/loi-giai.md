# Lời giải — Buổi 4.1

## Core — Vệt chạy

```python
import time, uuid

def new_trace():
    return {"trace_id": str(uuid.uuid4()), "steps": []}

def log_step(trace, name, **fields):
    trace["steps"].append({"step": name, "t": time.time(), **fields})

trace = new_trace()
log_step(trace, "retrieve", query=q, k=10, doc_ids=[d.id for d in docs])
log_step(trace, "generate", model="claude-sonnet-5", n_context=len(docs), stop_reason=r.stop_reason)
log_step(trace, "final", answer_len=len(answer), cited=bool(citations))
# Lưu vào store tra cứu được theo trace_id (dict/DB/file jsonl).
```
**Rubric:** trace có id + ≥ 3 bước (2đ); tra cứu được theo id (1đ).

## Đi sâu — Lần ngược
Field thiếu điển hình: phiên bản của doc trong `doc_ids`. **Rubric:** lần ngược < 2 phút (2đ); nêu field thiếu (1đ).

## Capstone
**Rubric:** trace chấm được cả ba mặt (2đ); không ghi nội dung nặng/nhạy cảm (1đ).
