# Lời giải — Buổi 4.2

## Core — Percentile

```python
def percentile(values, p):
    s = sorted(values)
    k = (len(s) - 1) * p / 100
    lo = int(k)
    if lo == k or lo + 1 >= len(s):
        return s[lo]
    return s[lo] + (s[lo + 1] - s[lo]) * (k - lo)

lat = [t["latency_ms"] for t in traces]
print("p50", percentile(lat, 50), "p95", percentile(lat, 95), "p99", percentile(lat, 99),
      "mean", sum(lat)/len(lat))
```
**Rubric:** ba percentile đúng (2đ); nêu khoảng cách p99 vs mean (1đ).

## Đi sâu — Caching
```python
system=[{"type": "text", "text": LONG_SYSTEM, "cache_control": {"type": "ephemeral"}}]
```
Rủi ro: context đổi nhẹ → cache miss; hoặc trúng cache trả context cũ. **Rubric:** hai con số chi phí (2đ);
một rủi ro cụ thể (1đ).

## Capstone
**Rubric:** nêu p50/p95/p99 + chi phí không cần tra (3đ).
