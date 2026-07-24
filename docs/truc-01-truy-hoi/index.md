# Trục 01 — Truy hồi

!!! quote "Câu hỏi trung tâm"
    Tại sao nó lấy sai tài liệu — và làm sao biết đó là lỗi truy hồi chứ không phải lỗi sinh?

Đây là trục **dễ dạy sai nhất**: kho kỹ thuật RAG có ba bốn chục món và ai cũng muốn dạy hết. Dạy **tám món cho
tới nơi**, kèm khả năng chẩn đoán nên dùng món nào, có giá trị hơn hẳn việc lướt qua ba mươi lăm món.

## Tám kỹ thuật được dạy sâu

| # | Kỹ thuật | Chữa đúng lỗi gì |
|---|---|---|
| 1 | Chunking theo cấu trúc | Chunk cắt ngang định nghĩa, khối mã, bảng tham số |
| 2 | Tìm kiếm lai (đặc + thưa) | Mã lỗi, tên hàm — embedding không bắt được |
| 3 | Lọc theo siêu dữ liệu | Đúng nội dung nhưng sai phiên bản/sản phẩm |
| 4 | Viết lại & tách truy vấn | Câu hỏi nhiều vế, hoặc từ ngữ khác tài liệu |
| 5 | Truy hồi giả định (HyDE) | Truy vấn quá ngắn, quá mơ hồ |
| 6 | Xếp hạng lại | Lấy đúng trong top-50 nhưng trượt top-5 |
| 7 | Bổ sung ngữ cảnh vào chunk | Chunk đúng nhưng tách ngữ cảnh thì vô nghĩa |
| 8 | Chunk nhỏ, trả về khối lớn | Khớp cần chính xác, trả lời cần đầy đủ |

## Bạn sẽ học gì

| Buổi | Nội dung |
|---|---|
| [Ca hỏng — Chunk cắt ngang](00-ca-hong.md) | Vì sao recall@10 nói dối khi chunk vỡ |
| [1.1 Đường cơ sở](1.1-duong-co-so/bai-giang.md) | Baseline tệ có chủ ý + cây chẩn đoán |
| [1.2 Chunking & siêu dữ liệu](1.2-chunking-sieu-du-lieu/bai-giang.md) | Hai đòn bẩy lớn nhất |
| [1.3 Lai ghép, viết lại, HyDE](1.3-lai-ghep-hyde/bai-giang.md) | Đặc + thưa, mở rộng truy vấn |
| [1.4 Xếp hạng lại](1.4-xep-hang-lai/bai-giang.md) | Từ bao phủ sang chính xác + ngân sách |

Thứ tự: **Ca hỏng → 1.1 → 1.2 → 1.3 → 1.4 → [Cổng 01](cong-01.md)**.

## Notebook nguồn

- [retrieval_augmented_generation](https://colab.research.google.com/github/anthropics/claude-cookbooks/blob/main/capabilities/retrieval_augmented_generation/guide.ipynb) — RAG 3 cấp + metric
- [contextual-embeddings](https://colab.research.google.com/github/anthropics/claude-cookbooks/blob/main/capabilities/contextual-embeddings/guide.ipynb) — contextual retrieval + hybrid BM25 + rerank
- [rag_using_pinecone](https://colab.research.google.com/github/anthropics/claude-cookbooks/blob/main/third_party/Pinecone/rag_using_pinecone.ipynb) — query rewriting
