# Mô hình trưởng thành & pitch định vị

Một khung để **khách tự soi mình vào** — công cụ thuyết phục mạnh nhất trong tư vấn, vì nó biến "anh đang thiếu"
thành "anh đang ở mức 2, đây là đường lên mức 3". Cộng với pitch để bạn mô tả chuyên môn trong 30 giây.

## Năm mức trưởng thành LLM sản xuất

Bám theo 5 trục — hệ phải vững trục trước mới lên mức sau.

### Mức 0 — Cảm tính
- **Dấu hiệu:** đánh giá bằng "nhìn thấy ổn"; không có bộ test; chọn model theo lời đồn.
- **Rủi ro:** mọi thay đổi là đánh bạc; không biết đang tốt lên hay xấu đi.
- **Lên mức 1:** dựng bộ đề vàng + một con số eval lặp lại được (Trục 00).

### Mức 1 — Đo được
- **Dấu hiệu:** có eval chạy được, giám khảo căn chỉnh (κ ≥ 0.6); quyết định dựa trên số.
- **Rủi ro:** biết hệ tệ ở đâu nhưng chưa chữa được gốc truy hồi/sinh.
- **Lên mức 2:** chẩn đoán và vá truy hồi (Trục 01).

### Mức 2 — Truy hồi vững
- **Dấu hiệu:** chunk theo cấu trúc, hybrid, lọc metadata, có bảng đóng góp.
- **Rủi ro:** lấy đúng tài liệu nhưng vẫn bịa/không biết từ chối.
- **Lên mức 3:** kiểm soát phần sinh — trung thành, trích dẫn, từ chối (Trục 02).

### Mức 3 — Trả lời đáng tin
- **Dấu hiệu:** trung thành ≥ 0.90, biết nói "không biết", trích dẫn kiểm chứng được.
- **Rủi ro:** thêm agent/tự động hoá mà không chứng minh cần, hoặc không đo độ tin cậy.
- **Lên mức 4:** dùng agent có kỷ luật + đo pass^k (Trục 03).

### Mức 4 — Sẵn sàng vận hành
- **Dấu hiệu:** vệt chạy lần ngược được, biết p50/p95/p99 + chi phí, eval chặn regression, kiểm bảo mật.
- **Rủi ro:** còn lại chủ yếu là tối ưu chi phí và mở rộng quy mô.
- **Đích:** hệ chịu được người dùng thật, tải thật, và kẻ tấn công thật.

!!! tip "Dùng trong tư vấn"
    Sau [audit](audit-checklist.md), chỉ cho khách họ đang ở mức nào và **một bước** lên mức kế. "Anh ở mức 1 —
    đo tốt rồi, nhưng truy hồi còn cắt chunk theo ký tự nên vẫn bịa. Vá cái đó là lên mức 2." Cụ thể, có lối ra,
    không phán xét.

## Pitch định vị

### Một dòng (bio / chữ ký)
> Tôi giúp đội ngũ **đưa hệ thống LLM từ demo lên sản phẩm** — tổ chức theo *vấn đề*, không theo công cụ, và
> *đo được* ở mọi bước.

### 30 giây (gặp gỡ, mở đầu)
> "Phần lớn dự án LLM kẹt ở chỗ chạy được demo nhưng không đo được, nên không biết đang tốt lên hay xấu đi. Tôi
> làm việc theo năm trục — đo lường, truy hồi, sinh, vòng lặp, vận hành — mỗi trục có một cổng bằng số phải vượt.
> Kết quả là hệ thống anh có thể *chứng minh* nó tốt, không phải *cảm thấy*."

### 2 phút (buổi tư vấn, có đất kể)
> "Tôi thấy ba lỗi lặp đi lặp lại ở các dự án LLM. Một: bỏ eval xuống cuối, nên mọi so sánh trước đó không kiểm
> chứng được. Tôi đảo nó lên đầu. Hai: nhầm 'lấy đúng tài liệu' với 'trả lời đúng' — recall cao mà vẫn bịa. Tôi
> tách hai loại lỗi và đo riêng. Ba: nhảy vào agent vì nó thời thượng, trong khi pipeline tất định rẻ hơn và đúng
> hơn. Tôi chứng minh bằng số khi nào thật sự cần agent.
>
> Cách tôi làm: một buổi audit chấm hệ của anh theo năm chiều, mỗi chiều một con số, ra ba việc đáng làm nhất.
> Từ đó anh quyết định bước tiếp — có tôi hay không."

### Biến tấu theo bối cảnh
- **Bán tư vấn:** nhấn "audit → bức tranh khách quan → lối ra rõ ràng".
- **Nội bộ (xin buy-in):** nhấn "eval-first tiết kiệm tiền, chặn regression, quyết định dựa trên số".
- **Thương hiệu:** biến mỗi luận điểm ngược dòng (eval-first, đừng-vội-agent, recall-nói-dối) thành một bài viết
  ngắn — mỗi bài một góc nhìn, tích luỹ thành uy tín.

!!! quote "Nguồn tự tin thật"
    Bạn tự tin không phải vì thuộc lòng câu chữ, mà vì đằng sau mỗi câu là một [bài phá trước](../truc-00-do-luong/00-ca-hong.md)
    bạn đã tự tay chạy và đo. Chạy thử vài ca hỏng trên corpus thật của mình trước khi đi tư vấn — khi đó bạn kể
    bằng trải nghiệm, không phải bằng slide.
