# Sổ tay luận điểm thuyết phục

Câu dao cạo để nói đúng lúc, và cách xoay phản biện. Mỗi luận điểm: **câu nói · vì sao nó thuyết phục · khi nào dùng.**

## Sáu luận điểm chủ lực

### 1. Eval-first — "Anh đo bằng gì?"
> *"Tôi không hỏi mô hình nào tốt hơn. Tôi hỏi anh đo bằng gì. Chưa có một lệnh cho ra một con số lặp lại được thì
> mọi so sánh sau đó chỉ là ý kiến."*

**Vì sao thuyết phục:** đảo ngược câu hỏi ai cũng hỏi (mô hình/công cụ) sang câu hỏi ít ai hỏi (phép đo). Lộ ra
bạn nghĩ như người vận hành, không phải người theo hype.
**Khi nào dùng:** ngay đầu buổi, khi khách sa đà so sánh model/framework.

### 2. Ngược dòng về agent — "Anh chắc mình cần agent chưa?"
> *"Câu đầu tiên tôi hỏi không phải xây agent thế nào, mà anh chắc mình cần agent chưa. Pipeline tất định rẻ hơn,
> dễ gỡ hơn, đúng hơn trong đa số ca. Agent chỉ đáng khi có ba dấu hiệu: số bước không biết trước, bước sau phụ
> thuộc bước trước, và có tín hiệu để tự sửa."*

**Vì sao thuyết phục:** giữa cơn sốt agent, người dám nói "khoan đã" là người có kinh nghiệm thật (và tiết kiệm
tiền cho khách).
**Khi nào dùng:** khi khách/sếp muốn "làm agent cho sang".

### 3. Con số làm cả phòng im lặng
> *"85% giám khảo đồng ý với người có thể tệ hơn tung đồng xu — nếu 80% mẫu cùng một nhãn. Phải đo Cohen κ, không
> phải tỉ lệ đồng ý."*
> *"pass@k đo khả năng, pass^k đo độ tin cậy. Người dùng gặp một lần chạy, không phải lần tốt nhất trong mười."*

**Vì sao thuyết phục:** một con số phản trực giác + một khái niệm sắc = tín hiệu rõ nhất của chuyên môn.
**Khi nào dùng:** khi cần "chốt hạ" uy tín trong 1 câu.

### 4. Bắt bài chỉ số dối
> *"recall@10 là chỉ số biết nói dối khi chunk không tự đủ nghĩa. Hệ vẫn 'lấy đúng tài liệu' theo mọi thước đo
> truy hồi, mà câu trả lời vẫn bịa — vì mô hình nhận nửa định nghĩa rồi điền nốt. Luôn ghép recall với một chỉ số
> ở đầu ra."*

**Vì sao thuyết phục:** cho thấy bạn không bị lừa bởi dashboard đẹp — bạn biết chỉ số nào che giấu điều gì.
**Khi nào dùng:** khi khách khoe "RAG của em recall cao lắm".

### 5. Tư duy ba chiều
> *"Mọi quyết định vận hành là bài toán ba chiều: chất lượng, độ trễ, chi phí. Ai chỉ báo cáo một chiều là đang
> giấu hai chiều còn lại. Rerank tăng 6 điểm chất lượng nhưng p99 gấp bốn và chi phí +40% — giữ hay bỏ phụ thuộc
> ngưỡng người dùng bỏ đi, chứ không phải con số chất lượng."*

**Vì sao thuyết phục:** nâng cuộc nói chuyện từ "kỹ thuật" lên "kinh doanh" — đúng thứ stakeholder cấp cao quan tâm.
**Khi nào dùng:** với người ra quyết định ngân sách/sản phẩm.

### 6. Bảo mật — "bộ ba chết người"
> *"Anh có bộ ba chết người chưa: dữ liệu riêng tư + nội dung không đáng tin + kênh gửi ra ngoài? Đủ ba thì một
> tài liệu độc người dùng tải lên có thể rút dữ liệu nội bộ ra — không cần hack, chỉ cần tiêm lệnh gián tiếp."*

**Vì sao thuyết phục:** chạm nỗi sợ cụ thể, đúng chuyên môn, và ít người nói được rành mạch.
**Khi nào dùng:** khi bàn triển khai/production, hoặc để tạo urgency.

## Xử lý phản biện

| Họ nói | Bạn đáp (có số) | Chốt |
|---|---|---|
| "Chỉ cần GPT/Gemini mạnh là đủ." | "Đổi mô hình mạnh hơn thường nhích vài điểm; viết lại mô tả công cụ/prompt thường nhảy vọt, chi phí bằng không. Phần lớn 'mô hình chưa đủ giỏi' thật ra là 'khung chạy chưa đủ tốt'." | Đo cả hai rồi quyết. |
| "Dùng mô hình lớn hơn cho chắc." | "Trước khi nâng cấp, tôi chứng minh khung chạy đã hết dư địa — gần như chưa bao giờ hết. Mô hình lớn hơn = độ trễ + chi phí + vẫn cùng lỗi khung." | Đắt hơn chưa chắc đúng hơn. |
| "RAG là xong rồi mà." | "RAG dừng ở truy hồi thì sản phẩm vẫn bịa. Lỗi sinh tách khỏi lỗi truy hồi: context đúng 100% mà vẫn bịa là chuyện thường — phải đo trần phần sinh riêng." | Truy hồi đúng ≠ trả lời đúng. |
| "Bọn em thấy nó chạy tốt rồi." | "Tốt theo cái gì? Nếu chưa có bộ đề vàng đủ sáu loại và một con số lặp lại được, 'thấy tốt' là cảm tính — và cảm tính không sống sót qua thay đổi tiếp theo." | Chưa đo được thì chưa biết. |
| "Eval tốn thời gian, ship trước đã." | "Eval là bảo hiểm: không có nó, mọi cải tiến sau này không kiểm chứng được, và một thay đổi âm thầm phá hệ mà không ai biết. Một lệnh ra một con số là đủ để bắt đầu." | Eval-first tiết kiệm, không phí. |
| "Agent là tương lai, làm agent hết đi." | "Agent đắt gấp nhiều lần, khó gỡ, mặt phẳng lỗi rộng. Nó chỉ thắng khi có ba dấu hiệu cụ thể — chứng minh bằng số, không phải cảm thấy." | Dùng đúng chỗ, không dùng cho sang. |

## Câu mở màn theo tình huống

- **Discovery call:** "Trước khi bàn giải pháp, cho tôi hỏi vài câu để hiểu hệ của anh đang hỏng ở đâu — thường
  chỉ 4-5 câu là ra." → chuyển sang [bộ câu hỏi chẩn đoán](cau-hoi-chan-doan.md).
- **Khách hoài nghi giá trị:** "Tôi đề xuất một buổi audit — chấm hệ của anh theo 5 cổng, mỗi cổng một con số.
  Xong anh có một bức tranh khách quan, quyết định thuê tôi hay không sau." → [audit](audit-checklist.md).
- **Thuyết trình/nội bộ:** mở bằng luận điểm 1 (eval-first) → khung 5 trục → mô hình trưởng thành.
