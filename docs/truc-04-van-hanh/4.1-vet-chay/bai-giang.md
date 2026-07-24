# 4.1 — Nhìn thấy được thì mới sửa được

!!! abstract "Mục tiêu"
    - Ghi vệt chạy có cấu trúc: ghi gì ở mỗi bước, và ghi gì thì thừa.
    - Lần ngược từ một khiếu nại của người dùng về đúng lượt gọi.
    - Ghi log để chấm được cả ba mặt: đầu ra, đường đi, trạng thái cuối.

## Vì sao vệt chạy đi trước sửa lỗi

Ở sản xuất, bạn không gỡ lỗi bằng cách chạy lại trên máy mình — sự cố đã xảy ra lúc 2 giờ sáng, trên dữ liệu bạn
không có. Thứ duy nhất còn lại là **vệt chạy** (trace). Không có nó, mọi khiếu nại đều là "không tái hiện được".

## Vệt chạy có cấu trúc

Mỗi truy vấn sinh một trace: một id, và một danh sách bước, mỗi bước ghi *đủ để tái dựng quyết định*.

```python
import time, uuid, json

def new_trace():
    return {"trace_id": str(uuid.uuid4()), "steps": []}

def log_step(trace, name, **fields):
    trace["steps"].append({"step": name, "t": time.time(), **fields})

# Ví dụ trong một truy vấn RAG-agent:
trace = new_trace()
log_step(trace, "retrieve", query=q, k=10, doc_ids=[d.id for d in docs], recall_hint=None)
log_step(trace, "generate", model="claude-sonnet-5", n_context=len(docs), stop_reason=r.stop_reason)
log_step(trace, "final", answer_len=len(answer), cited=bool(citations))
```

**Ghi gì:** đầu vào quyết định (query, doc_ids, tham số), kết quả mỗi bước, và mốc thời gian. **Ghi gì thừa:**
toàn bộ nội dung tài liệu (nặng, trùng), thông tin nhạy cảm không cần cho gỡ lỗi.

<div class="predict" markdown>
**Dự đoán:** Một người dùng khiếu nại "trợ lý trả lời sai về phiên bản". Với vệt chạy ở trên, bạn cần *tối thiểu*
những field nào để biết lỗi ở truy hồi hay ở sinh?

<textarea class="predict-input" placeholder="Viết dự đoán của bạn — dài ít nhất một câu..."></textarea>
<button class="predict-btn">Mở kết quả</button>

<div class="predict-result" hidden markdown>
Cần `doc_ids` đã lấy (bước retrieve) và phiên bản của các doc đó. Nếu **doc đúng phiên bản không nằm trong
`doc_ids`** → lỗi **truy hồi**. Nếu nó có trong `doc_ids` nhưng câu trả lời vẫn sai phiên bản → lỗi **sinh**.
Đây chính là cây chẩn đoán ở Trục 01/02, giờ áp lên dữ liệu sản xuất thật. Nếu vệt chạy không ghi `doc_ids`,
bạn không phân biệt được — và mọi khiếu nại thành "không tái hiện được".
</div>
</div>

## Lần ngược từ khiếu nại (bài tập bấm giờ)

Cho một `trace_id` từ khiếu nại, bạn phải tới được đúng lượt gọi model trong **< 2 phút**. Điều kiện: trace được
lưu tra cứu được theo id, và mỗi bước đủ trường để tái dựng.

## Ba mặt có thể chấm

| Mặt | Ghi gì để chấm được |
|---|---|
| **Đầu ra** | Câu trả lời cuối + có trích dẫn không |
| **Đường đi** | Chuỗi bước, tool nào gọi, thứ tự |
| **Trạng thái cuối** | Trạng thái phiên/bộ nhớ sau khi xong |

<div class="tool-justify" markdown>
**Thẻ biện minh — vệt chạy có cấu trúc**

- **Thay bằng gì vẫn chạy?** `print`/log văn bản rời rạc.
- **Gỡ ra thì chỉ số nào tụt?** Thời gian lần ngược sự cố (từ vài phút lên hàng giờ), tỉ lệ khiếu nại "không tái hiện được".
</div>

## Lỗi thường gặp

- Ghi log dạng văn bản tự do → không truy vấn/chấm được.
- Ghi cả nội dung tài liệu vào trace → nặng, rò rỉ dữ liệu.
- Không có `trace_id` xuyên suốt → không lần ngược được.

## Tóm tắt

Vệt chạy có cấu trúc, đủ để tái dựng quyết định và lần ngược từ khiếu nại. Ghi đầu vào quyết định + kết quả +
thời gian; đừng ghi nội dung nặng.

→ Tiếp: [4.2 — Độ trễ và chi phí là chỉ số hạng nhất](../4.2-do-tre-chi-phi/bai-giang.md)
