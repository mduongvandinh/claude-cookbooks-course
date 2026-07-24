# Lời giải — Buổi 0.1

## Core — Mã hoá mở

Không có "đáp án" cố định (phụ thuộc corpus), nhưng một kết quả đạt trông như:

| Nhóm lỗi | Tần suất (/30) |
|---|---|
| Trả lời theo sai phiên bản | 7 |
| Bịa mã lỗi / tên hàm không tồn tại | 5 |
| Bỏ sót điều kiện biên trong tài liệu | 4 |
| Trả lời câu ngoài phạm vi thay vì từ chối | 4 |
| Trộn thông tin hai sản phẩm | 3 |

**Rubric:** ≥ 5 nhóm tách bạch (2đ); có tần suất (1đ); đối chiếu với dự đoán ban đầu (1đ).

## Đi sâu — Xếp hạng theo ảnh hưởng

Ví dụ: "bịa mã lỗi" tần suất thấp hơn "sai phiên bản" nhưng nghiêm trọng hơn (dẫn người dùng chạy lệnh sai) →
xếp cao hơn. **Rubric:** có cột nghiêm trọng (1đ); một ví dụ nhóm hiếm-nghiêm trọng xếp cao (2đ).

## Capstone — Chốt corpus

**Rubric:** corpus có phiên bản + mã lỗi + ≥ 1 mâu thuẫn thật (2đ); action layer ≥ 2 mock tool, mô tả rõ đầu
vào/đầu ra (2đ).
