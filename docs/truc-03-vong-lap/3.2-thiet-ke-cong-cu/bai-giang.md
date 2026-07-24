# 3.2 — Thiết kế công cụ là thiết kế agent

[:material-notebook: Mở customer_service_agent trên Colab](https://colab.research.google.com/github/anthropics/claude-cookbooks/blob/main/tool_use/customer_service_agent.ipynb){ .md-button }

!!! abstract "Mục tiêu"
    - Chứng minh mô tả công cụ mơ hồ sinh agent ngu — bằng thực nghiệm.
    - Đo **độ chính xác chọn công cụ** như một chỉ số riêng.
    - Đặt ranh giới công cụ: một công cụ một việc.

## Mô tả công cụ mơ hồ → agent ngu

Nối tiếp ca hỏng: `search`/`lookup`/`find` cho độ chính xác chọn công cụ 0.55. Mô tả tốt nêu rõ **tìm gì, phạm
vi nào, trả về gì, khi nào không dùng**:

```python
tools = [{
    "name": "get_customer_info",
    "description": "Tra cứu thông tin khách hàng theo customer_id. Trả về tên, email, số điện thoại. "
                   "Dùng khi cần thông tin liên hệ; KHÔNG dùng để tra chi tiết đơn hàng.",
    "input_schema": {"type": "object",
        "properties": {"customer_id": {"type": "string", "description": "Mã định danh khách hàng."}},
        "required": ["customer_id"]},
}]
```

## Vòng lặp tool use nhiều bước

Từ customer_service_agent (model chuẩn hoá `claude-opus-4-8`) — lặp tới khi không còn gọi tool:

```python
while response.stop_reason == "tool_use":
    tool_use = next(b for b in response.content if b.type == "tool_use")
    tool_result = process_tool_call(tool_use.name, tool_use.input)
    messages = [
        {"role": "user", "content": user_message},
        {"role": "assistant", "content": response.content},
        {"role": "user", "content": [{"type": "tool_result",
            "tool_use_id": tool_use.id, "content": str(tool_result)}]},
    ]
    response = client.messages.create(model=MODEL_NAME, max_tokens=4096, tools=tools, messages=messages)
```

## Đo độ chính xác chọn công cụ

<div class="predict" markdown>
**Dự đoán:** Bạn có một bộ 50 câu, mỗi câu có "công cụ đúng cần gọi". Dự đoán: đo độ chính xác chọn công cụ tách
khỏi chất lượng đầu ra có ích gì?

<textarea class="predict-input" placeholder="Viết dự đoán của bạn — dài ít nhất một câu..."></textarea>
<button class="predict-btn">Mở kết quả</button>

<div class="predict-result" hidden markdown>
Tách được **nguyên nhân**: nếu đầu ra sai mà công cụ chọn đúng → lỗi ở sinh/tool logic; nếu công cụ chọn sai →
lỗi ở mô tả công cụ. Không tách thì bạn "đổ lỗi mô hình" mù mờ (đúng như ca hỏng). Độ chính xác chọn công cụ là
chỉ số riêng, Cổng 03 yêu cầu ≥ 0.90.
</div>
</div>

<div class="tool-justify" markdown>
**Thẻ biện minh — mô tả công cụ chi tiết**

- **Thay bằng gì vẫn chạy?** Mô tả một từ (`search`).
- **Gỡ ra thì chỉ số nào tụt?** Độ chính xác chọn công cụ — chi phí sửa bằng không, hiệu quả hơn đổi mô hình.
</div>

## Ranh giới công cụ

Một công cụ làm **một việc** và trả về thứ mô hình đọc được. Công cụ ôm đồm nhiều việc làm mô hình bối rối và khó
đo độ chính xác chọn.

## Lỗi thường gặp

- Mô tả công cụ mơ hồ/đồng nghĩa.
- Không đo độ chính xác chọn công cụ tách khỏi đầu ra.
- Công cụ ôm đồm nhiều việc.

## Tóm tắt

Thiết kế công cụ chính là thiết kế agent; mô tả rõ ràng > đổi mô hình; đo độ chính xác chọn công cụ riêng; một
công cụ một việc.

→ Tiếp: [3.3 — Trạng thái và trí nhớ](../3.3-trang-thai-tri-nho/bai-giang.md)
