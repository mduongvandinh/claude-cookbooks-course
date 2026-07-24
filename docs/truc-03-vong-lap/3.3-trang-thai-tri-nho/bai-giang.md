# 3.3 — Trạng thái và trí nhớ

[:material-notebook: Mở memory_cookbook trên Colab](https://colab.research.google.com/github/anthropics/claude-cookbooks/blob/main/tool_use/memory_cookbook.ipynb){ .md-button }

!!! abstract "Mục tiêu"
    - Phân biệt ba tầng: sổ nháp trong lượt, trạng thái phiên, trí nhớ dài hạn.
    - Hiểu vì sao đa số hệ thống không cần tầng thứ ba.
    - Thấy trí nhớ sai còn tệ hơn không có trí nhớ.

## Ba tầng thường bị gộp làm một

| Tầng | Là gì | Tồn tại bao lâu |
|---|---|---|
| **Sổ nháp trong lượt** | kết quả trung gian trong một truy vấn | một lượt |
| **Trạng thái phiên** | lịch sử hội thoại, biến phiên | một phiên |
| **Trí nhớ dài hạn** | kiến thức lưu qua nhiều phiên khác nhau | vĩnh viễn |

<div class="predict" markdown>
**Dự đoán:** Trợ lý tài liệu của bạn có cần tầng thứ ba (trí nhớ dài hạn qua nhiều phiên) không? Làm sao chứng
minh?

<textarea class="predict-input" placeholder="Viết dự đoán của bạn — dài ít nhất một câu..."></textarea>
<button class="predict-btn">Mở kết quả</button>

<div class="predict-result" hidden markdown>
**Đa số không cần.** Trợ lý tra tài liệu chỉ cần sổ nháp (trong lượt) + trạng thái phiên (hội thoại). Trí nhớ
dài hạn chỉ cần khi hệ phải *học và áp dụng* điều gì đó qua các phiên độc lập (ví dụ nhớ sở thích người dùng).
Chứng minh bằng cách chỉ ra một tác vụ **thất bại nếu không có** trí nhớ dài hạn — nếu không chỉ ra được, bạn
không cần nó, và thêm nó chỉ tăng rủi ro.
</div>
</div>

## Trí nhớ dài hạn (Claude 4) — khi thật sự cần

memory_cookbook dùng **memory tool** (client-side, lưu file) + **context editing** để giữ ngữ cảnh gọn:

```python
response = client.beta.messages.create(
    model="claude-sonnet-5",
    messages=messages,
    tools=[{"type": "memory_20250818", "name": "memory"}],
    betas=["context-management-2025-06-27"],
    context_management={"edits": [
        {"type": "clear_tool_uses_20250919",
         "trigger": {"type": "input_tokens", "value": 5000},
         "keep": {"type": "tool_uses", "value": 2}},
    ]},
)
```

Session 1 học một pattern → lưu vào `/memories` → Session 2 (hội thoại mới) áp dụng lại.

## Trí nhớ sai tệ hơn không có

<div class="tool-justify" markdown>
**Thẻ biện minh — trí nhớ dài hạn**

- **Thay bằng gì vẫn chạy?** Trạng thái phiên (không lưu qua phiên).
- **Gỡ ra thì chỉ số nào tụt?** Chỉ tụt nếu có tác vụ cần học-qua-phiên; nếu không, trí nhớ dài hạn thêm rủi ro
  **memory poisoning** (lỗi được lưu và tái dùng) — tệ hơn không có.
</div>

Bảo mật memory tool: kiểm đường dẫn (mọi path bắt đầu `/memories`, chặn traversal), cô lập theo người dùng/dự án,
lọc nội dung nhúng lệnh độc (nối Trục 04 — tiêm lệnh gián tiếp).

## Lỗi thường gặp

- Gộp ba tầng làm một → thêm trí nhớ dài hạn không cần thiết.
- Không chứng minh nhu cầu tầng ba.
- Lưu trí nhớ không kiểm chứng → poisoning.

## Tóm tắt

Ba tầng riêng biệt; đa số chỉ cần hai tầng đầu; chứng minh nhu cầu tầng ba trước khi thêm; trí nhớ sai tệ hơn
không có.

→ Tiếp: [3.4 — Chấm agent](../3.4-cham-agent/bai-giang.md)

---

**Tài liệu buổi này:** [Instructor notes](instructor-notes.md) · [Bài tập](bai-tap.md) · [Lời giải](loi-giai.md) · [Slide outline](slide-outline.md)
