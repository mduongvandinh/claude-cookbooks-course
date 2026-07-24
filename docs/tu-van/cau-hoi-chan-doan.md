# Bộ câu hỏi chẩn đoán

Hỏi để **lộ ra bạn thấy vấn đề của họ trước cả khi họ kể**. Mỗi câu kèm cột "câu trả lời của họ tiết lộ gì" — đó
là cách bạn chẩn đoán ngay tại bàn. Hỏi 4-6 câu là đủ để định vị hệ của họ nằm ở trục nào.

!!! tip "Cách dùng"
    Đừng hỏi cả bảng. Bắt đầu bằng câu Trục 00; câu trả lời sẽ chỉ bạn nhảy tới trục nào tiếp theo. Người nghe sẽ
    cảm thấy bạn "đọc được" hệ của họ.

## Trục 00 — Đo lường (luôn hỏi trước)

| Câu hỏi | Trả lời tiết lộ |
|---|---|
| "Anh biết hệ tốt lên hay xấu đi bằng cách nào?" | "Nhìn thấy cảm giác ổn" = chưa có eval → gốc rễ mọi vấn đề nằm đây. |
| "Bộ test của anh có bao nhiêu câu, và mấy loại?" | Toàn câu dữ kiện = bộ đề vô dụng (không bao giờ trượt). |
| "Ai chấm đúng/sai, và họ đồng thuận với nhau bao nhiêu?" | Không đo κ = con số eval không đáng tin. |
| "Chạy lại eval hai lần có ra cùng con số không?" | Không tái lập được = không thể chặn regression. |

## Trục 01 — Truy hồi

| Câu hỏi | Trả lời tiết lộ |
|---|---|
| "Chunk của anh cắt theo gì — số ký tự hay cấu trúc?" | Cắt ký tự = chunk vỡ nghĩa = sinh bịa dù recall cao. |
| "Người dùng tìm mã lỗi/tên hàm — anh dùng embedding hay cả từ khoá?" | Chỉ embedding = trượt lớp truy vấn định danh → cần hybrid. |
| "Nó có bao giờ trả lời đúng nội dung nhưng sai phiên bản không?" | Có = thiếu lọc metadata; và họ thường không nhận ra đây là lỗi riêng. |
| "recall của anh cao — nhưng anh đo chất lượng ở đầu ra bằng gì?" | Chỉ đo recall = đang bị chỉ số dối ru ngủ. |

## Trục 02 — Sinh

| Câu hỏi | Trả lời tiết lộ |
|---|---|
| "Khi context đã đúng, nó còn bịa không? Anh đo tỉ lệ đó chưa?" | Chưa đo = không biết trần phần sinh, đổ hết lỗi cho truy hồi. |
| "Hệ có biết nói 'không có trong tài liệu' không, và từ chối nhầm bao nhiêu?" | Chỉ đo một trong hai = chưa hiểu hai chỉ số kéo nhau. |
| "Câu trả lời có trích dẫn — trích dẫn đó có thật hay mô hình tự bịa?" | Trích dẫn do prompt = có thể bịa; chưa dùng cơ chế kiểm chứng. |

## Trục 03 — Vòng lặp (agent)

| Câu hỏi | Trả lời tiết lộ |
|---|---|
| "Vì sao anh chọn agent thay vì pipeline tất định — có đo không?" | "Vì agent hiện đại" = chọn theo hype, chưa chứng minh cần. |
| "Độ chính xác chọn công cụ của agent là bao nhiêu?" | Không đo = không biết lỗi ở mô tả công cụ hay ở mô hình. |
| "Agent chạy 10 lần đúng mấy lần — và anh báo cáo pass@k hay pass^k?" | Chỉ pass@k = đang giấu độ may rủi thật của sản phẩm. |
| "Có `max_steps` chưa?" | Chưa = rủi ro vòng vô hạn/đốt chi phí. |

## Trục 04 — Vận hành

| Câu hỏi | Trả lời tiết lộ |
|---|---|
| "Một người dùng khiếu nại lúc 2 giờ sáng — anh mất bao lâu lần ra đúng lượt gọi?" | "Không tái hiện được" = thiếu vệt chạy có cấu trúc. |
| "p50/p95/p99 và chi phí mỗi truy vấn của hệ là bao nhiêu?" | Trả lời bằng "trung bình" = đang giấu cái đuôi. |
| "Hệ có bộ ba chết người không (riêng tư + không đáng tin + kênh ra)?" | Đủ ba mà chưa có người duyệt = lỗ hổng tiêm lệnh gián tiếp. |
| "Eval có tự chạy và chặn khi điểm tụt không?" | Không = regression âm thầm, mọi cải tiến có thể bị phá. |

## Câu hỏi tổng — dùng để chốt

> *"Nếu tôi lấy repo của anh và người khác chạy đúng code đó, họ có ra cùng kết quả không? Nếu tôi đổi vị trí hai
> câu trả lời khi chấm, thứ hạng có đổi không? Nếu tôi hỏi một câu ngoài tài liệu, nó bịa hay nói không biết?"*

Ba câu này gói cả năm trục. Người trả lời trôi chảy cả ba là người đã làm thật — và người *hỏi* được cả ba cũng vậy.
