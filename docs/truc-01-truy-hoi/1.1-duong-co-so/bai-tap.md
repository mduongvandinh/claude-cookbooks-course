# Bài tập — Buổi 1.1

## Core — Dựng baseline + recall@k
**Dự đoán trước:** recall@10 của baseline trên corpus của bạn sẽ khoảng bao nhiêu?

Nhiệm vụ: dựng baseline (chunk cố định + voyage-2 + dot-product), đo recall@k tại k = 1,3,5,10,20.

**Tiêu chí đạt:** có đường cong recall@k; so với dự đoán.

## Đi sâu — Cây chẩn đoán
**Dự đoán trước:** lỗi của bạn thuộc nhánh nào (index / lấy về / xếp hạng)?

Nhiệm vụ: với 5 câu trượt, phân loại theo cây chẩn đoán 3 nhánh, kèm bằng chứng.

**Tiêu chí đạt:** 5 câu phân nhánh đúng, mỗi câu có bằng chứng (có trong index? top-20?).

## Capstone — Baseline cho trợ lý
Dựng baseline RAG cho "Trợ lý tài liệu nội bộ", ghi recall@10 làm mốc.

**Tiêu chí đạt:** baseline chạy được, recall@10 ghi lại làm mốc cho các buổi sau.
