# Cheat sheet — Eval harness

Bộ khung tối thiểu để chấm và căn chỉnh, dùng xuyên suốt Trục 00.

## Khởi tạo + chạy một prompt

```python
from anthropic import Anthropic
import re
from collections import Counter
client = Anthropic()
MODEL_NAME = "claude-sonnet-5"

def get_completion(messages, max_tokens=2048):
    return client.messages.create(model=MODEL_NAME, max_tokens=max_tokens, messages=messages).content[0].text
```

## Chấm bằng model (single-output, theo rubric)

Mẫu từ notebook `building_evals`: giám khảo suy nghĩ trong `<thinking>`, rồi xuất một nhãn nhị phân trong
`<correctness>`, ta parse bằng regex.

```python
def build_grader_prompt(answer, rubric):
    content = (
        "Bạn được cho một câu trả lời và một rubric.\n"
        f"<answer>{answer}</answer>\n<rubric>{rubric}</rubric>\n"
        "Suy nghĩ trong <thinking></thinking>. Sau đó xuất 'correct' hoặc 'incorrect' trong <correctness></correctness>."
    )
    return [{"role": "user", "content": content}]

def grade(output, rubric):
    completion = get_completion(build_grader_prompt(output, rubric))
    m = re.search(r"<correctness>(.*?)</correctness>", completion, re.DOTALL)
    if not m:
        raise ValueError("Không tìm thấy thẻ <correctness>")
    return m.group(1).strip()
```

## Cohen κ — đo đồng thuận giám khảo vs người

Không có trong cookbook, viết bằng stdlib thuần. Đo mức đồng thuận **vượt trên may rủi** — khác hẳn "tỉ lệ
đồng ý" thô.

```python
def cohen_kappa(a, b):
    n = len(a)
    po = sum(1 for x, y in zip(a, b) if x == y) / n         # đồng ý quan sát được
    ca, cb = Counter(a), Counter(b)
    pe = sum((ca[k] / n) * (cb[k] / n) for k in set(a) | set(b))  # đồng ý do may rủi
    return 1.0 if pe == 1 else (po - pe) / (1 - pe)
```

## Bảng `tool_choice`

| Giá trị | Nghĩa |
|---|---|
| `{"type": "auto"}` | Claude tự quyết có gọi tool hay không |
| `{"type": "any"}` | Bắt buộc gọi một tool bất kỳ |
| `{"type": "tool", "name": "..."}` | Ép đúng một tool cụ thể (hữu ích để lấy structured output) |
