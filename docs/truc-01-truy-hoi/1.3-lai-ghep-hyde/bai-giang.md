# 1.3 — Lai ghép, viết lại truy vấn, HyDE

!!! abstract "Mục tiêu"
    - Hiểu vì sao BM25 vẫn thắng ở lớp mã lỗi/tên định danh.
    - Hoà điểm hai nguồn (đặc + thưa) bằng trọng số **đo được**.
    - Biết HyDE cải thiện ở đâu, làm tệ ở đâu.

## Vì sao cần tìm kiếm lai

<div class="predict" markdown>
**Dự đoán:** Người dùng tìm mã lỗi `ERR_CONN_4021` hoặc tên hàm `retryWithBackoff`. Dự đoán: embedding ngữ
nghĩa (voyage-2) hay BM25 (từ khoá) sẽ tìm đúng hơn?

<textarea class="predict-input" placeholder="Viết dự đoán của bạn — dài ít nhất một câu..."></textarea>
<button class="predict-btn">Mở kết quả</button>

<div class="predict-result" hidden markdown>
**BM25 thắng.** Mã lỗi và tên định danh là chuỗi ký tự chính xác — embedding ngữ nghĩa "hiểu" ý nghĩa nhưng
không bắt được khớp chuỗi hiếm. Ngược lại, câu hỏi diễn đạt tự nhiên ("làm sao thử lại khi mất kết nối") thì
embedding thắng. Vì thế cần **lai ghép** — dùng cả hai, hoà điểm.
</div>
</div>

## Hoà điểm đặc + thưa (hybrid)

Từ notebook contextual-embeddings: semantic và BM25 mỗi bên lấy 150 ứng viên, hoà bằng reciprocal-rank có
trọng số (mặc định semantic 0.8, BM25 0.2 — **trọng số phải đo, không đoán**):

```python
# index: vị trí trong danh sách xếp hạng của mỗi nguồn
score = 0.0
score += semantic_weight * (1 / (semantic_rank + 1))
score += bm25_weight     * (1 / (bm25_rank + 1))
```

BM25 nên index **cả** nội dung chunk **và** câu ngữ cảnh sinh ở buổi 1.2.

## Viết lại / mở rộng truy vấn

Kỹ thuật #4: cho Claude sinh nhiều từ khoá tìm kiếm đa dạng, mỗi cái truy vấn riêng rồi gộp kết quả (từ notebook
Pinecone):

```python
def keyword_prompt(question):
    return (f"...sinh danh sách 5 từ khoá tìm kiếm rất đa dạng cho câu hỏi:\n{question}\n"
            'Xuất dạng JSON có một thuộc tính "keywords".')
# Mỗi từ khoá embed + truy vấn top_k=3, gộp kết quả.
```

## HyDE — dùng đúng chỗ

HyDE (truy hồi giả định): sinh một câu trả lời *giả* rồi nhúng nó để tìm. Cải thiện với truy vấn **quá ngắn/mơ
hồ**; nhưng **làm tệ đi** khi câu hỏi đã rất cụ thể (thêm nhiễu + độ trễ). Đây là ví dụ điển hình của "kỹ thuật
làm tệ đi" mà Cổng 01 yêu cầu bạn nêu.

<div class="tool-justify" markdown>
**Thẻ biện minh — tìm kiếm lai (BM25 + embedding)**

- **Thay bằng gì vẫn chạy?** Chỉ embedding.
- **Gỡ ra thì chỉ số nào tụt?** Recall trên mã lỗi/tên hàm — chính lớp câu hỏi mà corpus kỹ thuật đầy rẫy.
</div>

## Lỗi thường gặp

- Chỉ dùng embedding → trượt mã lỗi/tên hàm.
- Đoán trọng số hoà điểm thay vì đo.
- Bật HyDE cho câu đã cụ thể → tệ hơn.

## Tóm tắt

Lai ghép đặc + thưa (trọng số đo được) + mở rộng truy vấn; HyDE chỉ cho câu mơ hồ. Đo từng cái vào bảng đóng góp.

→ Tiếp: [1.4 — Xếp hạng lại và bài toán ngân sách](../1.4-xep-hang-lai/bai-giang.md)

---

**Tài liệu buổi này:** [Instructor notes](instructor-notes.md) · [Bài tập](bai-tap.md) · [Lời giải](loi-giai.md) · [Slide outline](slide-outline.md)
