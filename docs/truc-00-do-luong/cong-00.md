# Cổng 00

Không qua cổng thì không sang [Trục 01](../index.md). Cổng **phân tầng**: ngưỡng *tối thiểu để đi tiếp* và
ngưỡng *đạt chuẩn* (mức Vững). Lớp hỗn hợp có buổi remediation nếu chưa đạt tối thiểu — không bỏ ai lại, nhưng
cũng không nới tiêu chí.

## Ba điều kiện (đều là số)

| Điều kiện | Tối thiểu để đi tiếp | Đạt chuẩn (Vững) |
|---|---|---|
| **Bộ đề vàng** | ≥ 24 câu, phủ đủ 6 loại, mỗi loại ≥ 2 | ≥ 30 câu, mỗi loại ≥ 3 |
| **Giám khảo** (so nhãn người, 50 mẫu giữ riêng) | Cohen κ ≥ 0.4 | Cohen κ ≥ 0.6 |
| **Tái lập** | Một lệnh CLI ra một con số; lặp 2 lần chênh < 2% | như tối thiểu |

## Ghi chú vận hành

- Chưa đạt **tối thiểu** → buổi remediation, không sang Trục 01.
- Đạt tối thiểu nhưng chưa đạt chuẩn → được đi tiếp, ghi nhận mức "Đạt" (chưa "Vững").
- 50 mẫu nhãn người phải **giữ riêng**, không nhìn vào cho tới lúc chấm giám khảo.
- "Một lệnh CLI" nghĩa là toàn bộ eval chạy được bằng một câu lệnh, ra đúng một con số — nền cho việc chặn
  regression tự động ở Trục 04.
