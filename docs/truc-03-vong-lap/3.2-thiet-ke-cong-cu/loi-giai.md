# Lời giải — Buổi 3.2

## Core — Viết lại mô tả
```python
# Trước: {"name": "search", "description": "search"}
# Sau:
{"name": "search_docs",
 "description": "Tìm trong tài liệu API theo từ khoá, trả về đoạn văn liên quan. "
                "Dùng cho câu hỏi cách dùng/cấu hình. KHÔNG dùng để tra bản ghi khách hàng."}
```
Độ chính xác chọn công cụ = (số câu chọn đúng công cụ) / (tổng câu). **Rubric:** hai con số trước/sau (2đ); chi
phí ~0 (1đ).

## Đi sâu — So ba cách
| Cách | Acc chọn công cụ | Chi phí |
|---|---|---|
| Mô tả tồi + mô hình mạnh | ~0.6 | cao |
| Mô tả tốt + mô hình cũ | ~0.9 | thấp |
| Cả hai | ~0.92 | cao |

**Rubric:** bảng ba cách (2đ); kết luận đúng (1đ).

## Capstone
**Rubric:** acc chọn công cụ ≥ 0.80 (2đ); mỗi công cụ một việc (1đ).
