# 3.1 — Khi nào không cần agent

[:material-notebook: Mở basic_workflows trên Colab](https://colab.research.google.com/github/anthropics/claude-cookbooks/blob/main/patterns/agents/basic_workflows.ipynb){ .md-button }

!!! abstract "Mục tiêu"
    - Nhận ra **ba dấu hiệu** thật sự cần vòng lặp.
    - Dựng cả pipeline tất định lẫn agent trên cùng tác vụ rồi đo.
    - Hiểu chi phí ẩn của agent.

## Ba dấu hiệu thật sự cần vòng lặp

<div class="predict" markdown>
**Dự đoán:** Tác vụ nào sau đây *cần* agent, tác vụ nào chỉ cần pipeline tất định: (a) phân loại ticket vào 5
nhóm; (b) điều tra một sự cố qua nhiều bước tuỳ kết quả từng bước?

<textarea class="predict-input" placeholder="Viết dự đoán của bạn — dài ít nhất một câu..."></textarea>
<button class="predict-btn">Mở kết quả</button>

<div class="predict-result" hidden markdown>
(a) **Pipeline tất định** — một lần phân loại, số bước biết trước. (b) **Agent** — số bước không biết trước, bước
sau phụ thuộc kết quả bước trước. Ba dấu hiệu cần vòng lặp: **(1)** số bước không biết trước; **(2)** bước sau
phụ thuộc kết quả bước trước; **(3)** có tín hiệu để tự sửa. Thiếu cả ba → dùng pipeline tất định, rẻ và đúng hơn.
</div>
</div>

## Pipeline tất định — thường là đủ

Nhiều tác vụ tưởng cần agent thật ra chỉ cần **chuỗi/định tuyến** tất định (từ basic_workflows, qua `util.llm_call`):

```python
from util import extract_xml, llm_call

def chain(input, prompts):                  # chuỗi các bước cố định
    result = input
    for p in prompts:
        result = llm_call(f"{p}\nInput: {result}")
    return result

def route(input, routes):                   # định tuyến tới prompt chuyên biệt
    sel = llm_call(f"Chọn nhóm phù hợp trong {list(routes.keys())}...\nInput: {input}")
    key = extract_xml(sel, "selection").strip().lower()
    return llm_call(f"{routes[key]}\nInput: {input}")
```

`util.llm_call` mặc định `claude-sonnet-5`. Số bước cố định, dễ gỡ lỗi, rẻ.

## Dựng cả hai rồi đo

Đừng tranh luận — **dựng cả hai bản** (tất định và agent) trên cùng tác vụ, đo chất lượng + độ trễ + chi phí.
Đây là bằng chứng Cổng 03 yêu cầu.

<div class="tool-justify" markdown>
**Thẻ biện minh — vòng lặp agent**

- **Thay bằng gì vẫn chạy?** Pipeline tất định (chain/route).
- **Gỡ ra thì chỉ số nào tụt?** Chỉ tụt khi tác vụ có đủ ba dấu hiệu; nếu không, agent chỉ thêm độ trễ, chi phí,
  và mặt phẳng lỗi rộng hơn.
</div>

## Chi phí ẩn của agent

Độ trễ nhân lên (nhiều lượt gọi), chi phí nhân lên, mặt phẳng lỗi rộng ra (mỗi bước một chỗ hỏng). Agent không
"miễn phí thông minh" — nó đắt và khó gỡ.

## Lỗi thường gặp

- Dùng agent cho tác vụ số bước biết trước.
- Tranh luận thay vì dựng cả hai bản rồi đo.
- Bỏ qua chi phí ẩn (độ trễ, mặt phẳng lỗi).

## Tóm tắt

Ba dấu hiệu cần vòng lặp; mặc định pipeline tất định; dựng cả hai rồi đo. Biết *khi nào không* dùng agent là kỹ
năng đầu tiên.

→ Tiếp: [3.2 — Thiết kế công cụ là thiết kế agent](../3.2-thiet-ke-cong-cu/bai-giang.md)

---

**Tài liệu buổi này:** [Instructor notes](instructor-notes.md) · [Bài tập](bai-tap.md) · [Lời giải](loi-giai.md) · [Slide outline](slide-outline.md)
