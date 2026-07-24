# Lời giải — Buổi 0

## Core — Chặn chia cho 0

```python
def run_tool(expression):
    try:
        return str(eval(expression))          # demo — production dùng parser an toàn
    except ZeroDivisionError:
        return "Lỗi: chia cho 0."
    except Exception as e:
        return f"Lỗi: biểu thức không hợp lệ ({e})."
```

**Rubric:** hỏi "10 chia 0" không crash (2đ); model nhận thông báo lỗi và trả lời (1đ).

## Đi sâu — Structured output lồng nhau

```python
tools = [{
    "name": "save_contact",
    "description": "Lưu một liên hệ.",
    "input_schema": {"type": "object", "properties": {
        "author": {"type": "object", "properties": {
            "name": {"type": "string"}, "email": {"type": "string", "format": "email"}},
            "required": ["name", "email"]}},
        "required": ["author"]},
}]
r = client.messages.create(model=MODEL_NAME, max_tokens=512, tools=tools,
    tool_choice={"type": "tool", "name": "save_contact"},
    messages=[{"role": "user", "content": "Liên hệ: Lan, email lan@vd.com"}])
contact = next(b.input for b in r.content if b.type == "tool_use")
# {'author': {'name': 'Lan', 'email': 'lan@vd.com'}}
```

**Rubric:** `input` có object lồng đủ `name` + `email` (2đ); ép được `tool_choice` (1đ).

## Capstone — `tro_ly.py`

```python
from anthropic import Anthropic
client = Anthropic()
MODEL_NAME = "claude-sonnet-5"

tools = [{"name": "calculator", "description": "Thực hiện phép tính số học.",
    "input_schema": {"type": "object", "properties": {"expression": {"type": "string"}},
        "required": ["expression"]}}]

def run_tool(expr):
    try:
        return str(eval(expr))
    except Exception as e:
        return f"Lỗi: {e}"

def hoi(cau_hoi):
    r = client.messages.create(model=MODEL_NAME, max_tokens=1024, tools=tools,
        messages=[{"role": "user", "content": cau_hoi}])
    if r.stop_reason == "tool_use":
        tu = next(b for b in r.content if b.type == "tool_use")
        r = client.messages.create(model=MODEL_NAME, max_tokens=1024, tools=tools, messages=[
            {"role": "user", "content": cau_hoi},
            {"role": "assistant", "content": r.content},
            {"role": "user", "content": [{"type": "tool_result", "tool_use_id": tu.id,
                "content": run_tool(tu.input["expression"])}]}])
    return r.content[0].text

if __name__ == "__main__":
    print(hoi("Tính 235 * 47 giúp tôi"))
```

**Rubric:** chạy được, trả lời có dùng tool (2đ); vòng 4 bước đúng (1đ).
