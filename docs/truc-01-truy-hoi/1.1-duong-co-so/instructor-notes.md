# Instructor notes — Buổi 1.1

**Thời lượng:** ~60 phút.

## Thông điệp chốt
1. Không baseline thì không đo được cải tiến — baseline tệ có chủ ý là mốc.
2. Đọc cả đường cong recall@k, không đọc một con số.
3. Cây chẩn đoán 3 nhánh định vị lỗi trước khi tối ưu.

## Câu hỏi gợi mở
- "Khoảng cách recall@5 vs recall@20 nói gì?" (lỗi xếp hạng vs lỗi index).
- "Vì sao không bỏ RAG, nhét hết tài liệu vào ngữ cảnh dài?" (nạp câu hỏi vàng).

## Điểm hay vấp
- Nhảy tối ưu khi chưa chẩn đoán. Đọc một con số recall.

## Gợi ý demo
Vẽ đường cong recall@k live; chỉ khoảng cách top-5 vs top-20.

## Nạp bộ câu hỏi vàng
- "recall@10 tăng 12 điểm nhưng chất lượng không đổi. Ba giải thích khả dĩ?"
