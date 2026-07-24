# Trục 03 — Vòng lặp

!!! quote "Câu hỏi trung tâm"
    Khi nào cần agent thay vì một pipeline tất định — và làm sao chứng minh chứ không phải cảm thấy?

Buổi đầu tiên của trục này dạy khi nào **không** nên dùng agent. Đây không phải khiêm tốn giả tạo: pipeline tất
định rẻ hơn, dễ gỡ lỗi hơn và đúng hơn trong phần lớn ca sử dụng. Học viên cần biết ca của mình thuộc loại nào
trước khi học dựng vòng lặp.

## Bạn sẽ học gì

| Buổi | Nội dung |
|---|---|
| [Ca hỏng — Công cụ mô tả tồi](00-ca-hong.md) | Đổi mô hình vs viết lại mô tả công cụ |
| [3.1 Khi nào không cần agent](3.1-khi-nao-khong-agent/bai-giang.md) | Ba dấu hiệu thật sự cần vòng lặp |
| [3.2 Thiết kế công cụ](3.2-thiet-ke-cong-cu/bai-giang.md) | Thiết kế công cụ là thiết kế agent |
| [3.3 Trạng thái & trí nhớ](3.3-trang-thai-tri-nho/bai-giang.md) | Ba tầng; trí nhớ sai tệ hơn không có |
| [3.4 Chấm agent](3.4-cham-agent/bai-giang.md) | pass@k vs pass^k; chấm đường đi |

Thứ tự: **Ca hỏng → 3.1 → 3.2 → 3.3 → 3.4 → [Cổng 03](cong-03.md)**.

## Notebook nguồn

- [basic_workflows](https://colab.research.google.com/github/anthropics/claude-cookbooks/blob/main/patterns/agents/basic_workflows.ipynb) — chain/parallel/route
- [orchestrator_workers](https://colab.research.google.com/github/anthropics/claude-cookbooks/blob/main/patterns/agents/orchestrator_workers.ipynb)
- [evaluator_optimizer](https://colab.research.google.com/github/anthropics/claude-cookbooks/blob/main/patterns/agents/evaluator_optimizer.ipynb)
- [memory_cookbook](https://colab.research.google.com/github/anthropics/claude-cookbooks/blob/main/tool_use/memory_cookbook.ipynb) — trạng thái & trí nhớ
- [customer_service_agent](https://colab.research.google.com/github/anthropics/claude-cookbooks/blob/main/tool_use/customer_service_agent.ipynb) — vòng lặp tool use

## Kết nối capstone

Sau trục này, trợ lý nâng thành **agent tự lập kế hoạch nhiều bước** — nhưng chỉ khi chứng minh được (bằng số)
nó thắng pipeline tất định.
