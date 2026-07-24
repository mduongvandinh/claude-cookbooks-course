# Cổng 03

Không qua cổng thì không sang [Trục 04](../truc-04-van-hanh/index.md). **Phân tầng**.

## Điều kiện (đều là số)

| Điều kiện | Tối thiểu để đi tiếp | Đạt chuẩn (Vững) |
|---|---|---|
| **Agent vs pipeline tất định** | chứng minh bằng số agent thắng (hoặc thua + giải thích) trên ≥ 1 nhóm | + phân tích khi nào nên/không nên |
| **Độ chính xác chọn công cụ** | ≥ 0.80 | ≥ 0.90 |
| **Báo cáo độ tin cậy** | có `pass@3` | + `pass^3` và khoảng cách hai con số |

## Ghi chú vận hành

- "Agent thắng" phải đo trên **cùng tác vụ**, cùng corpus — dựng cả hai bản rồi so.
- `pass^k` (mọi lần đều đúng) đo độ tin cậy sản xuất; `pass@k` (ít nhất một lần đúng) đo khả năng. Sản phẩm cần
  cái đầu — nêu rõ khoảng cách giữa hai con số.
- Nếu agent **thua** pipeline tất định mà bạn giải thích được vì sao, đó vẫn là vượt cổng — trục này dạy *khi nào
  không* dùng agent.
