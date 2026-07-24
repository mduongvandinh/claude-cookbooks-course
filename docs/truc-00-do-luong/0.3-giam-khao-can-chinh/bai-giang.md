# 0.3 — Bộ chấm và bài toán căn chỉnh

[:material-notebook: Mở building_evals trên Colab](https://colab.research.google.com/github/anthropics/claude-cookbooks/blob/main/misc/building_evals.ipynb){ .md-button }

!!! abstract "Mục tiêu"
    - Hiểu vì sao **nhãn nhị phân** ổn định hơn thang 1–5.
    - Nhận diện các thiên lệch của giám khảo: vị trí, độ dài, tự ưu ái.
    - Căn chỉnh giám khảo với người bằng **Cohen κ**, không phải "tỉ lệ đồng ý".

## Nhãn nhị phân thay vì thang 1–5

Thang liên tục làm cả người chấm lẫn giám khảo bất nhất: ranh giới 3 vs 4 mơ hồ, mỗi lần chấm một khác, κ tụt.
Nhãn **correct/incorrect** ổn định và đủ để phát hiện một thay đổi làm tốt lên hay tệ đi.

## Giám khảo bằng model + parse

Mẫu từ `building_evals`: giám khảo suy nghĩ trong `<thinking>`, xuất một nhãn trong `<correctness>`.

```python
from anthropic import Anthropic
import re
from collections import Counter
client = Anthropic()
MODEL_NAME = "claude-sonnet-5"

def get_completion(messages, max_tokens=2048):
    return client.messages.create(model=MODEL_NAME, max_tokens=max_tokens, messages=messages).content[0].text

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

## Các thiên lệch của giám khảo

- **Vị trí** — chọn câu xuất hiện trước (đã thấy ở [ca hỏng](../00-ca-hong.md)).
- **Độ dài** — nhầm câu dài/trôi chảy là câu đúng.
- **Tự ưu ái** — ưu ái câu do chính họ (cùng model) sinh ra.

Bản khử position bias (nối lại ca hỏng):

```python
def judge_pair_debiased(question, ans_a, ans_b):
    v1 = judge_once(question, ans_a, ans_b)   # A ở vị trí đầu
    v2 = judge_once(question, ans_b, ans_a)   # A ở vị trí sau
    picks_a = (v1 == "A") + (v2 == "B")
    if picks_a == 2: return "A"
    if picks_a == 0: return "B"
    return "hoà"
```

## Căn chỉnh bằng Cohen κ

<div class="predict" markdown>
**Dự đoán:** Giám khảo đồng ý 85% với nhãn người. Dự đoán κ là bao nhiêu nếu **80% mẫu** là nhãn 'correct'?

<textarea class="predict-input" placeholder="Viết dự đoán của bạn — dài ít nhất một câu..."></textarea>
<button class="predict-btn">Mở kết quả</button>

<div class="predict-result" hidden markdown>
κ **thấp một cách đáng báo động** — quanh 0.06. Vì nếu 80% mẫu là 'correct', chỉ cần đoán 'correct' mọi lúc
cũng đã đúng ~80% (hoặc hơn). "Đồng ý do may rủi" (pₑ) ở đây rất cao, nên κ = (0.85 − pₑ)/(1 − pₑ) gần như bằng
0. Đây chính là lý do 85% đồng ý có thể **tệ hơn tung đồng xu**: nó chỉ phản ánh tỉ lệ nền, không phản ánh
năng lực phân biệt của giám khảo.
</div>
</div>

```python
def cohen_kappa(a, b):
    n = len(a)
    po = sum(1 for x, y in zip(a, b) if x == y) / n
    ca, cb = Counter(a), Counter(b)
    pe = sum((ca[k] / n) * (cb[k] / n) for k in set(a) | set(b))
    return 1.0 if pe == 1 else (po - pe) / (1 - pe)
```

<div class="tool-justify" markdown>
**Thẻ biện minh — model làm giám khảo**

- **Thay bằng gì vẫn chạy?** Người chấm tay toàn bộ (chậm, đắt, không quy mô được).
- **Gỡ ra thì chỉ số nào tụt?** Tốc độ và quy mô chấm — nhưng chỉ hợp lệ *sau khi* κ ≥ ngưỡng so với người.
</div>

## Lỗi thường gặp

- Báo cáo "tỉ lệ đồng ý" thay vì κ → che mất tỉ lệ nền.
- Không khử position bias trước khi đo → κ bẩn.
- Tinh chỉnh giám khảo trên tập đã dùng để đo κ → rò rỉ.

## Tóm tắt

Nhãn nhị phân + khử thiên lệch + đo κ so với người. Giám khảo chỉ được tin khi κ vượt ngưỡng cổng.

→ Tiếp: [Cổng 00](../cong-00.md)
