# Trục 02 — Sinh

!!! quote "Câu hỏi trung tâm"
    Context đã đúng hoàn toàn. Vì sao nó vẫn bịa — và làm sao dạy nó nói "tôi không biết"?

Phần lớn khoá học RAG dừng ở truy hồi và coi phần sinh là chuyện của prompt. Đó là lý do sản phẩm của học viên
**vẫn bịa** sau khi ra lớp. Trục này tách lỗi sinh khỏi lỗi truy hồi và xử lý riêng.

## Bạn sẽ học gì

| Buổi | Nội dung |
|---|---|
| [Ca hỏng — Ngữ cảnh cám dỗ](00-ca-hong.md) | Mạch lạc bị nhầm thành đáng tin |
| [2.1 Tách hai loại lỗi](2.1-tach-loi/bai-giang.md) | Trung thành vs hữu ích; trích dẫn cấp câu |
| [2.2 Ngữ cảnh dài & mâu thuẫn](2.2-ngu-canh-dai/bai-giang.md) | Lost-in-the-middle, phân xử phiên bản |
| [2.3 Từ chối trả lời](2.3-tu-choi/bai-giang.md) | Nói "không biết" mà không thành cỗ máy từ chối |

Thứ tự: **Ca hỏng → 2.1 → 2.2 → 2.3 → [Cổng 02](cong-02.md)**.

## Notebook nguồn

- [using_citations](https://colab.research.google.com/github/anthropics/claude-cookbooks/blob/main/misc/using_citations.ipynb) — trích dẫn cấp câu (Citations API)
- [summarization](https://colab.research.google.com/github/anthropics/claude-cookbooks/blob/main/capabilities/summarization/guide.ipynb) — grounding "Not specified"
- [building_moderation_filter](https://colab.research.google.com/github/anthropics/claude-cookbooks/blob/main/misc/building_moderation_filter.ipynb) — phân loại/từ chối

## Kết nối capstone

Sau trục này, trợ lý **trung thành với tài liệu + trích dẫn nguồn + biết từ chối** khi câu hỏi ngoài phạm vi.
