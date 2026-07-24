# Trục 00 — Đo lường

!!! quote "Câu hỏi trung tâm"
    Làm sao biết hệ thống đang tốt lên hay xấu đi — mà không phải nhìn rồi cảm thấy?

Trục này đi **trước tất cả** vì nó là điều kiện cần của bốn trục còn lại. Không có nó, cả khoá học biến thành
một chuỗi ý kiến: mọi khẳng định "kỹ thuật A tốt hơn B" ở các trục sau đều không kiểm chứng được. Đây cũng là trục
học viên ghét nhất trong hai buổi đầu và biết ơn nhất ở tuần thứ chín.

## Bạn sẽ học gì

| Buổi | Vấn đề giải quyết |
|---|---|
| [Ca hỏng — Giám khảo hỏng](00-ca-hong.md) | Vì sao một giám khảo chưa kiểm định làm hỏng mọi thí nghiệm |
| [0.1 Phân tích lỗi](0.1-phan-tich-loi/bai-giang.md) | Đọc dữ liệu thật trước khi nghĩ tới chỉ số |
| [0.2 Bộ đề vàng](0.2-bo-de-vang/bai-giang.md) | Sáu loại câu hỏi; vì sao bộ đề toàn dữ kiện là vô dụng |
| [0.3 Giám khảo & căn chỉnh](0.3-giam-khao-can-chinh/bai-giang.md) | Nhãn nhị phân, position bias, Cohen κ |

Thứ tự đề xuất: **Ca hỏng → 0.1 → 0.2 → 0.3 → [Cổng 00](cong-00.md)**.

## Chốt corpus + action layer (làm ở buổi 0.1)

Ngay buổi 0.1, mỗi học viên chốt **corpus riêng** (kho tài liệu kỹ thuật một sản phẩm) và giữ nguyên tới hết
khoá. Kèm theo là một **action layer** — vài mock tool/API (tra bản ghi, cập nhật trạng thái, mở ticket) — để
trục 03 sau này có action surface thật. Đổi corpus giữa chừng = phá khả năng so sánh giữa các trục.

## Notebook nguồn

- [building_evals](https://colab.research.google.com/github/anthropics/claude-cookbooks/blob/main/misc/building_evals.ipynb) — bốn phần của một eval, ba cách chấm
- [generate_test_cases](https://colab.research.google.com/github/anthropics/claude-cookbooks/blob/main/misc/generate_test_cases.ipynb) — sinh test case tự động

!!! warning "Cookbook không có sẵn phần lõi của trục này"
    Pairwise judge, position bias, Cohen κ, calibration — không notebook nào trong cookbook làm. Ta viết từ đầu
    (stdlib thuần), bám các nguồn ngoài (Hamel Husain, Shreya Shankar, Eugene Yan) về mặt khái niệm.

## Kết nối capstone

Sau trục này, "Trợ lý tài liệu nội bộ" của bạn có một **bộ eval đo được chất lượng trả lời của chính nó** —
điều kiện để mọi cải tiến ở trục sau kiểm chứng được.
