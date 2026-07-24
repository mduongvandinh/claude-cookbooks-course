# Sổ lỗi & test case (toàn khoá)

Đây là hiện thân của **quy tắc ③ (bánh cóc)** dành cho học viên: mỗi lỗi từng gặp trở thành một ca kiểm thử
vĩnh viễn, **chỉ thêm không xoá**. Sổ này quay một chiều — một lỗi đã vào đây thì ở lại mãi, kể cả sau khi đã
sửa, để nó không bao giờ tái diễn mà không ai biết.

| Lỗi | Nguyên nhân | Test case kiểm lại |
|---|---|---|
| Đo A vs B mà không hoán đổi vị trí | Position bias — đo thiên lệch vị trí của giám khảo thay vì chất lượng | Chạy lại cả hai chiều, so tỉ lệ thắng của *vị trí thứ nhất*; nếu vẫn ~60–65% thì là thiên lệch |

> Mỗi buổi, thêm dòng mới cho lỗi vừa phát sinh. Không xoá dòng cũ.
