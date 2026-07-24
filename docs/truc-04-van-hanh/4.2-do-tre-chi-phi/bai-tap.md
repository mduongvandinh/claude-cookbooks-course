# Bài tập — Buổi 4.2

## Core — Đo p50/p95/p99
**Dự đoán trước:** p99 của hệ bạn gấp mấy lần trung bình?

Nhiệm vụ: thu latency của ≥ 50 truy vấn, tính p50/p95/p99 bằng `percentile`, so với trung bình.

**Tiêu chí đạt:** ra ba percentile; nêu khoảng cách p99 vs trung bình.

## Đi sâu — Prompt caching
**Dự đoán trước:** bật cache cho system prompt dài sẽ giảm chi phí input bao nhiêu %?

Nhiệm vụ: thêm `cache_control` cho phần context lặp, đo chi phí input trước/sau.

**Tiêu chí đạt:** hai con số chi phí; nêu một rủi ro cache invalidation cụ thể.

## Capstone — Bảng số liệu trợ lý
Ghi p50/p95/p99 + chi phí mỗi truy vấn của "Trợ lý tài liệu nội bộ".

**Tiêu chí đạt:** nêu được bốn con số không cần tra cứu.
