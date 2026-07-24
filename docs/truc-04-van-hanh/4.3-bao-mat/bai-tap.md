# Bài tập — Buổi 4.3

## Core — Kiểm bộ ba chết người
**Dự đoán trước:** trợ lý của bạn có mấy phần trong ba (riêng tư / không đáng tin / kênh ra)?

Nhiệm vụ: liệt kê từng phần của bộ ba trong hệ capstone; nếu đủ ba, đề xuất bỏ/giảm một phần.

**Tiêu chí đạt:** phân tích rõ ba phần; một đề xuất giảm rủi ro cụ thể.

## Đi sâu — Dựng thử tiêm lệnh gián tiếp
**Dự đoán trước:** agent có làm theo lệnh ẩn trong tài liệu không?

Nhiệm vụ: nhúng một lệnh độc vào một tài liệu corpus, cho agent đọc, quan sát hành vi; thêm một biện pháp chặn.

**Tiêu chí đạt:** tái hiện được (hoặc chặn được) tiêm lệnh; mô tả biện pháp.

## Capstone — Chốt khoá eval-chặn
Gắn eval Cổng 00 vào một script chạy trước mỗi thay đổi, chặn khi điểm tụt quá ngưỡng.

**Tiêu chí đạt:** một lệnh chạy eval, trả exit code khác 0 khi tụt quá ngưỡng.
