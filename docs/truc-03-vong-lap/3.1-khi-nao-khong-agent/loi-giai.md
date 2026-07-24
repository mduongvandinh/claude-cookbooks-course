# Lời giải — Buổi 3.1

## Core — Cả hai bản
```python
# Tất định
from util import llm_call
def pipeline_tat_dinh(x):
    return chain(x, [PROMPT_B1, PROMPT_B2])
# Agent: vòng while stop_reason == "tool_use" (xem 3.2)
# Đo: chất lượng (eval), độ trễ (percentile), chi phí (tokens mọi lượt)
```
**Rubric:** ba cặp số hai bản (2đ); kết luận có bằng chứng (1đ).

## Đi sâu — Ba dấu hiệu
**Rubric:** phân tích 3 dấu hiệu (2đ); nhất quán với số Core (1đ).

## Capstone
**Rubric:** quyết định có số đo hỗ trợ (2đ).
