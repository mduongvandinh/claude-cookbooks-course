# 0.2 — Bộ đề vàng và sáu loại câu hỏi

[:material-notebook: Mở generate_test_cases trên Colab](https://colab.research.google.com/github/anthropics/claude-cookbooks/blob/main/misc/generate_test_cases.ipynb){ .md-button }

!!! abstract "Mục tiêu"
    - Hiểu **sáu loại câu hỏi** và vì sao thiếu loại nào thì bộ đề "mù" chỗ đó.
    - Biết tự sinh câu hỏi bằng model — dùng ở đâu, hỏng ở đâu.
    - Tách tập giữ riêng ngay từ đầu.

## Vì sao bộ đề toàn dữ kiện là vô dụng

<div class="predict" markdown>
**Dự đoán:** Bộ đề 30 câu của bạn có 28 câu dữ kiện ("API này nhận tham số gì?"). Dự đoán: nó sẽ nói gì *sai
lệch* về hệ thống của bạn?

<textarea class="predict-input" placeholder="Viết dự đoán của bạn — dài ít nhất một câu..."></textarea>
<button class="predict-btn">Mở kết quả</button>

<div class="predict-result" hidden markdown>
Nó **không bao giờ trượt**. Câu dữ kiện dễ — gần như mọi cấu hình đều trả lời đúng, nên bộ đề không phân biệt
được cấu hình tốt và cấu hình tệ. Bạn sẽ thấy điểm ~95% và tưởng hệ thống ổn, trong khi nó hỏng nặng ở đúng
những chỗ bộ đề không chạm tới: câu biên, câu ngoài phạm vi, câu đối kháng.
</div>
</div>

## Sáu loại câu hỏi

| Loại | Đo cái gì |
|---|---|
| **Dữ kiện** | Trả lời trực tiếp có trong tài liệu |
| **Thời gian/phiên bản** | Có chọn đúng phiên bản không (hỏi v3, đừng trả v1) |
| **Biên** | Điều kiện giới hạn, giá trị mặc định, ngoại lệ |
| **Ngoài phạm vi** | Có từ chối đúng khi tài liệu không chứa câu trả lời không |
| **Đối kháng** | Câu hỏi gài, giả định sai, cố dụ model bịa |
| **Nhất quán** | Cùng câu hỏi diễn đạt khác nhau, trả lời có ổn định không |

Bộ đề tốt phải phủ **cả sáu**, mỗi loại đủ số lượng — vì mỗi loại soi một kiểu lỗi khác nhau đã tìm thấy ở
buổi 0.1.

## Tự sinh câu hỏi bằng model

Sinh nhanh nhưng phải người duyệt. Pattern từ `generate_test_cases`:

```python
from anthropic import Anthropic
client = Anthropic()
MODEL_NAME = "claude-sonnet-5"

def sinh_cau_hoi(loai, tai_lieu, so_luong=3):
    prompt = (
        f"Từ tài liệu sau, sinh {so_luong} câu hỏi thuộc loại '{loai}'.\n"
        f"<tai_lieu>{tai_lieu}</tai_lieu>\n"
        "Mỗi câu hỏi trong một thẻ <q></q>."
    )
    import re
    out = client.messages.create(model=MODEL_NAME, max_tokens=1024, temperature=1,
        messages=[{"role": "user", "content": prompt}]).content[0].text
    return re.findall(r"<q>(.*?)</q>", out, re.DOTALL)

SAU_LOAI = ["dữ kiện", "thời gian/phiên bản", "biên", "ngoài phạm vi", "đối kháng", "nhất quán"]
```

<div class="tool-justify" markdown>
**Thẻ biện minh — tự sinh câu hỏi bằng model**

- **Thay bằng gì vẫn chạy?** Viết tay từng câu.
- **Gỡ ra thì chỉ số nào tụt?** Tốc độ tạo đề và độ phủ — nhưng phải trả giá bằng người duyệt, vì model sinh
  lệch về câu dễ và nhiễm khuynh hướng của chính nó.
</div>

??? note "Đi sâu — tách tập giữ riêng"
    Tách ~20% bộ đề làm **tập giữ riêng**, không nhìn vào cho tới lúc chấm giám khảo (buổi 0.3). Nếu bạn tinh
    chỉnh rubric dựa trên tập này, nó không còn "sạch" để đo κ nữa.

## Lỗi thường gặp

- Bộ đề lệch về câu dễ (dữ kiện) → điểm cao giả tạo.
- Sinh bằng model rồi dùng luôn không duyệt → nhiễm khuynh hướng của model.
- Không tách tập giữ riêng → không đo được κ trung thực ở 0.3.

## Tóm tắt

Sáu loại câu hỏi, mỗi loại soi một kiểu lỗi. Tự sinh được nhưng phải người duyệt. Giữ riêng 20% cho 0.3.

→ Tiếp: [0.3 — Bộ chấm và bài toán căn chỉnh](../0.3-giam-khao-can-chinh/bai-giang.md)
