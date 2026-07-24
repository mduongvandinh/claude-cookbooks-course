# Bài tập — Buổi 0.3

## Core — Tính κ so với người

**Dự đoán trước:** giám khảo của bạn sẽ đồng ý với nhãn người bao nhiêu %? Và κ tương ứng là bao nhiêu?

Nhiệm vụ: chấm 50 mẫu (giữ riêng từ 0.2) bằng `grade`, so với nhãn người, tính `cohen_kappa`.

**Tiêu chí đạt:** ra được κ; đối chiếu với dự đoán; giải thích khoảng cách giữa "tỉ lệ đồng ý" và κ.

## Đi sâu — Khử position bias

**Dự đoán trước:** κ sẽ tăng hay giảm sau khi khử position bias bằng chạy hai chiều?

Nhiệm vụ: với bộ chấm so cặp, đo κ trước và sau khi dùng `judge_pair_debiased`. So sánh.

**Tiêu chí đạt:** hai giá trị κ (trước/sau), giải thích chiều thay đổi.

## Bước capstone — Chốt giám khảo cho trợ lý

Căn chỉnh giám khảo cho "Trợ lý tài liệu nội bộ" tới **κ ≥ 0.4** (tối thiểu Cổng 00) trên 50 mẫu giữ riêng.

**Tiêu chí đạt:** κ ≥ 0.4; một lệnh CLI ra một con số điểm; lặp 2 lần chênh < 2%.
