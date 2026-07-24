# Bài tập — Buổi 3.4

## Core — Đo pass@k và pass^k
**Dự đoán trước:** agent của bạn pass^3 sẽ là bao nhiêu?

Nhiệm vụ: chạy agent k=5 lần trên mỗi tác vụ của một bộ nhỏ; tính pass@3 và pass^3; nêu khoảng cách.

**Tiêu chí đạt:** hai con số; giải thích khoảng cách nói gì về độ tin cậy.

## Đi sâu — Chấm đường đi
**Dự đoán trước:** có ca nào kết quả đúng mà đường đi phải đánh trượt không?

Nhiệm vụ: thêm `max_steps`; định nghĩa một tiêu chí đường đi (ví dụ không gọi tool ghi khi chỉ cần đọc); chấm.

**Tiêu chí đạt:** một ca kết-quả-đúng-đường-đi-sai bị bắt; có max_steps.

## Capstone — Chấm agent trợ lý + Cổng 03
Đạt độ chính xác chọn công cụ ≥ 0.80, báo cáo pass^3, chứng minh agent vs pipeline.

**Tiêu chí đạt:** ba yêu cầu Cổng 03 tối thiểu đạt.
