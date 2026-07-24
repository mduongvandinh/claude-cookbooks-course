# Instructor notes — Buổi 1.2

**Thời lượng:** ~60 phút.

## Thông điệp chốt
1. Câu hỏi đúng là "chunk có tự đủ nghĩa không", không phải "bao nhiêu token".
2. Contextual retrieval gắn ngữ cảnh trước khi nhúng — nhớ prompt caching.
3. Lọc metadata cứng chữa lỗi sai phiên bản.

## Câu hỏi gợi mở
- "Hai chunk cùng size, khác cách cắt — recall vs trung thành khác nhau thế nào?"
- "Vì sao phải cache tài liệu khi sinh ngữ cảnh?"

## Điểm hay vấp
- Cắt theo ký tự. Bỏ metadata. Sinh ngữ cảnh không cache → chi phí vọt.

## Gợi ý demo
Cho một khối mã bị cắt đôi → mô hình bịa; chunk theo cấu trúc → đúng.

## Nạp bộ câu hỏi vàng
- "Vì sao chunk 512 token? Không được trả lời 'vì mặc định'."
