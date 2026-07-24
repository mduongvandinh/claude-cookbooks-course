# Bài tập — Buổi 1.2

## Core — Chunk theo cấu trúc
**Dự đoán trước:** đổi từ cắt-ký-tự sang cắt-theo-cấu-trúc, recall@10 đổi bao nhiêu? Còn độ trung thành?

Nhiệm vụ: thay bộ chunk sang cắt theo mục/khối mã; đo recall@10 và một chỉ số đầu ra trước/sau.

**Tiêu chí đạt:** hai cặp số (recall, đầu ra) trước/sau; giải thích chênh lệch.

## Đi sâu — Contextual retrieval + metadata
**Dự đoán trước:** gắn ngữ cảnh làm Pass@10 tăng bao nhiêu?

Nhiệm vụ: sinh ngữ cảnh cho chunk (cache tài liệu), nhúng `context + chunk`; thêm lọc metadata phiên bản.

**Tiêu chí đạt:** Pass@10 trước/sau; một truy vấn chứng minh lọc phiên bản đúng.

## Capstone — Nâng chunking trợ lý
Chuyển trợ lý sang chunk cấu trúc + metadata; ghi vào bảng đóng góp.

**Tiêu chí đạt:** recall@10 tăng so với mốc 1.1; bảng đóng góp có 2 dòng.
