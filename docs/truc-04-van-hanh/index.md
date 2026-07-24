# Trục 04 — Vận hành

!!! quote "Câu hỏi trung tâm"
    Nó hỏng thế nào lúc 2 giờ sáng, và bạn biết được sau bao lâu?

Đây là trục **không có kho notebook nào dạy**, và cũng là trục phân biệt người xây demo với người xây sản phẩm.
Toàn bộ nội dung tự soạn — bù lại, nó là phần khiến khoá học của bạn không thể thay thế bằng một danh sách liên kết.

## Bạn sẽ học gì

| Buổi | Vấn đề giải quyết |
|---|---|
| [Ca hỏng — Đánh đổi](00-ca-hong.md) | Vì sao "giữ hay bỏ" là câu hỏi bẫy khi chỉ nhìn hai con số |
| [4.1 Vệt chạy](4.1-vet-chay/bai-giang.md) | Nhìn thấy được thì mới sửa được |
| [4.2 Độ trễ & chi phí](4.2-do-tre-chi-phi/bai-giang.md) | p50/p95/p99, chi phí mỗi truy vấn là chỉ số hạng nhất |
| [4.3 Bảo mật](4.3-bao-mat/bai-giang.md) | Bộ ba chết người, tiêm lệnh gián tiếp, chặn regression |

Thứ tự: **Ca hỏng → 4.1 → 4.2 → 4.3 → [Cổng 04 (Tốt nghiệp)](cong-04.md)**.

## Notebook nguồn (tham khảo)

- [prompt_caching](https://colab.research.google.com/github/anthropics/claude-cookbooks/blob/main/misc/prompt_caching.ipynb) — giảm chi phí/độ trễ
- [batch_processing](https://colab.research.google.com/github/anthropics/claude-cookbooks/blob/main/misc/batch_processing.ipynb) — xử lý lô
- [usage_cost_api](https://colab.research.google.com/github/anthropics/claude-cookbooks/blob/main/observability/usage_cost_api.ipynb) — theo dõi chi phí

## Kết nối capstone

Sau trục này, "Trợ lý tài liệu nội bộ" có vệt chạy lần ngược được, biết p50/p95/p99 + chi phí của chính nó, và
eval tự động chặn khi điểm tụt — tức là **sẵn sàng sản xuất**.
