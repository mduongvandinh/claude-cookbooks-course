# Lời giải — Buổi 2.1

## Core — Thí nghiệm cô lập
```python
# context perfect: nhét đúng đoạn chứa câu trả lời, bỏ qua truy hồi
faithful = [grade(ans, rubric) for ans, rubric in zip(answers_perfect_ctx, rubrics)]
tran = 1 - faithful.count("correct") / len(faithful)   # tỉ lệ bịa còn lại
```
**Rubric:** con số trần (2đ); đối chiếu dự đoán (1đ).

## Đi sâu — Citations API
```python
for block in response.content:
    if block.type == "text" and getattr(block, "citations", None):
        for c in block.citations:
            print(c.cited_text, "—", c.document_title)
```
**Rubric:** trích dẫn trỏ đúng nguồn đã cấp (3đ). API không trả trích dẫn ngoài nguồn.

## Capstone
**Rubric:** trợ lý trả lời kèm trích dẫn kiểm chứng được (2đ).
