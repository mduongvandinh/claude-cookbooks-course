# Instructor notes — Buổi 4.2

**Thời lượng:** ~60 phút.

## Thông điệp chốt
1. Trung bình giấu cái đuôi — luôn đọc p50/p95/p99.
2. Người dùng cảm nhận TTFT, không phải thời gian hoàn tất.
3. Tính chi phí đủ mọi lượt gọi (agent lặp) + nhúng + rerank.

## Câu hỏi gợi mở
- "Trung bình 800ms nói gì về người dùng chậm nhất?" (gần như không gì).
- "Prompt caching có rủi ro gì?" (cache invalidation, trúng cache sai).

## Điểm hay vấp
- Báo cáo trung bình. Quên lượt gọi lặp của agent. Cache context động.

## Gợi ý demo
Tính percentile live trên một mẫu latency lệch đuôi — cho thấy p99 gấp nhiều lần trung bình.

## Nạp bộ câu hỏi vàng
- "Xếp hạng lại làm p99 tăng gấp bốn. Giữ hay bỏ? Cần thêm số liệu gì?"
- "Chi phí mỗi truy vấn của bạn là bao nhiêu? Nếu chưa trả lời được thì thiếu gì?"
