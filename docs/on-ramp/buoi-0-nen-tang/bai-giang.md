# Buổi 0 — Nền tảng: gọi được Claude và một vòng tool use

[:material-notebook: Mở calculator_tool trên Colab](https://colab.research.google.com/github/anthropics/claude-cookbooks/blob/main/tool_use/calculator_tool.ipynb){ .md-button }

!!! abstract "Mục tiêu"
    - Gọi được Messages API và đọc kết quả.
    - Hiểu **bốn bước** của một vòng tool use single-turn.
    - Ép model trả về **structured output** bằng tool.

## Vì sao có buổi này

Trục 00 giả định bạn đã gọi được API và định nghĩa được tool. Buổi này trang bị đúng phần nền đó cho người mới,
để cả lớp cùng một điểm xuất phát.

## 1. Gọi API cơ bản

```python
from anthropic import Anthropic
client = Anthropic()               # đọc ANTHROPIC_API_KEY từ môi trường
MODEL_NAME = "claude-sonnet-5"

msg = client.messages.create(
    model=MODEL_NAME, max_tokens=1024,
    messages=[{"role": "user", "content": "Tóm tắt đoạn sau trong 1 câu: ..."}],
)
print(msg.content[0].text)
```

`messages` là danh sách lượt hội thoại; mỗi lượt có `role` (`user`/`assistant`) và `content`. Kết quả nằm ở
`msg.content` — một danh sách các khối; khối văn bản có `.text`.

## 2. Một vòng tool use

Claude **không tự tính** số lớn chính xác. Ta cho nó một tool `calculator`; khi cần, nó *yêu cầu* gọi tool,
**bạn** chạy tool, rồi gửi kết quả trở lại.

<div class="predict" markdown>
**Dự đoán:** Với câu "Tính 1984135 * 9343116", Claude sẽ trả về ngay đáp số, hay trả về một yêu cầu gọi tool trước?

<textarea class="predict-input" placeholder="Viết dự đoán của bạn..."></textarea>
<button class="predict-btn">Mở kết quả</button>

<div class="predict-result" hidden markdown>
Nó trả về một **yêu cầu gọi tool**: `stop_reason == "tool_use"`, và trong `content` có một khối `tool_use`
với `input = {"expression": "1984135 * 9343116"}`. Claude không tự tính — nó nhờ tool.
</div>
</div>

```python
tools = [{
    "name": "calculator",
    "description": "Thực hiện phép tính số học.",
    "input_schema": {
        "type": "object",
        "properties": {"expression": {"type": "string"}},
        "required": ["expression"],
    },
}]

# (a) Gọi lần 1 — Claude quyết định dùng tool
r = client.messages.create(model=MODEL_NAME, max_tokens=1024, tools=tools,
    messages=[{"role": "user", "content": "Tính 1984135 * 9343116"}])

# (b) Đọc stop_reason, lấy khối tool_use
if r.stop_reason == "tool_use":
    tu = next(b for b in r.content if b.type == "tool_use")
    # (c) BẠN chạy tool
    result = str(eval(tu.input["expression"]))   # demo — eval KHÔNG an toàn cho production
    # (d) Gửi tool_result trở lại, gọi lần 2
    r2 = client.messages.create(model=MODEL_NAME, max_tokens=1024, tools=tools, messages=[
        {"role": "user", "content": "Tính 1984135 * 9343116"},
        {"role": "assistant", "content": r.content},
        {"role": "user", "content": [{"type": "tool_result", "tool_use_id": tu.id, "content": result}]},
    ])
    print(r2.content[0].text)
```

**Bốn bước:** (a) gọi với `tools=` → (b) đọc `stop_reason == "tool_use"` → (c) chạy tool → (d) gửi
`tool_result` (kèm `tool_use_id`) và gọi lại. Model chỉ *yêu cầu*; **code của bạn** mới thực thi.

<div class="tool-justify" markdown>
**Thẻ biện minh — tool `calculator`**

- **Thay bằng gì vẫn chạy?** Để Claude tự tính — nhưng nó sai với số lớn.
- **Gỡ ra thì chỉ số nào tụt?** Độ chính xác số học.
</div>

## 3. Structured output bằng tool

Định nghĩa một tool làm "khuôn" JSON, rồi **ép** gọi bằng `tool_choice`, và đọc `input` của khối tool_use
(không cần chạy tool).

```python
tools2 = [{
    "name": "print_sentiment_scores",
    "description": "In điểm cảm xúc.",
    "input_schema": {"type": "object", "properties": {
        "positive": {"type": "number"}, "negative": {"type": "number"}, "neutral": {"type": "number"}},
        "required": ["positive", "negative", "neutral"]},
}]

r3 = client.messages.create(model=MODEL_NAME, max_tokens=1024, tools=tools2,
    tool_choice={"type": "tool", "name": "print_sentiment_scores"},
    messages=[{"role": "user", "content": "Sản phẩm này tuyệt vời!"}])
scores = next(b.input for b in r3.content if b.type == "tool_use")   # {'positive': ..., ...}
```

??? note "Đi sâu"
    - `eval()` ở phần 2 chỉ để demo — production phải dùng parser an toàn (ví dụ `ast.literal_eval` với kiểm
      tra, hoặc một thư viện tính toán).
    - `tool_choice`: `{"type":"auto"}` (Claude tự quyết), `{"type":"any"}` (bắt buộc gọi một tool),
      `{"type":"tool","name":...}` (ép đúng một tool) — dùng cái cuối để chắc chắn có structured output.

## Lỗi thường gặp

- **Quên `tool_use_id`** trong `tool_result` → API báo lỗi ghép cặp.
- **Kiểm tra sai `stop_reason`** (dùng `"end_turn"` thay vì `"tool_use"`) → bỏ lỡ nhánh gọi tool.
- **Quên đính `r.content`** (lượt assistant) vào lịch sử trước khi gửi `tool_result`.

## Tóm tắt

Một vòng tool use gồm 4 bước; model yêu cầu, bạn thực thi. Structured output là tool use "một chiều" — chỉ đọc
`input`. Hai ý này là nền cho toàn khoá.

→ Tiếp: [Trục 00 — Đo lường](../../truc-00-do-luong/index.md)
