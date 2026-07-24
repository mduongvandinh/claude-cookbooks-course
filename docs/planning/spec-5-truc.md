# Thiết kế: Giáo trình 5 trục — "Không đo được thì không dạy được"

**Ngày:** 2026-07-24 (viết lại từ bản 10-module theo khung 5 trục của người dùng)
**Trạng thái:** Đã chốt kiến trúc, chờ review spec
**Nguồn chân lý:** Khung syllabus HTML "Giáo trình 5 trục" do người dùng thiết kế + bộ Claude Cookbooks (87 notebooks)

## 0. Vì sao viết lại

Bản spec đầu (10 module theo năng lực: Tool Use → Multimodal → RAG → Agents → Evals → Production)
đi theo **trục tài liệu** — gom bài theo cách cookbook tự phân loại. Khung 5 trục của người dùng đi theo
**trục vấn đề**, và mạnh hơn ở ba điểm quyết định:

1. **Đảo Eval lên đầu.** Nếu Eval nằm cuối, mọi khẳng định "kỹ thuật A tốt hơn B" ở các phần trước
   không kiểm chứng được suốt khoá — học viên học một danh mục thay vì một môn.
2. **Cổng bằng số.** Mỗi trục kết bằng một cổng có tiêu chí định lượng, không cãi nhau được.
3. **Một corpus xuyên suốt.** Điểm số giữa các trục chỉ có nghĩa khi đo trên cùng bộ dữ liệu.

Spec này thay thế hoàn toàn kiến trúc 10 module. Bốn quy tắc sư phạm, capstone tinh thần, và định dạng
MkDocs → Pages được giữ nhưng tổ chức lại quanh 5 trục.

## 1. Mục tiêu

Dựng giáo trình để người dùng **đứng lớp dạy một khoá bootcamp 9–10 tuần** về xây ứng dụng LLM sản xuất,
tổ chức theo 5 trục vấn đề, eval-first, có cổng định lượng. Học viên tốt nghiệp phải **chẩn đoán được một
hệ thống chưa từng thấy**, không chỉ dùng được một danh mục kỹ thuật.

## 2. Bối cảnh & ràng buộc (đã chốt)

| Yếu tố | Quyết định |
|---|---|
| Đối tượng | Hỗn hợp trình độ → cần **on-ramp Buổi 0** cho người mới (xem §4) |
| Định dạng dạy | **Cohort/bootcamp** (cổng, calibration, đổi máy cần lớp đồng bộ). *Cần người dùng xác nhận: khác lựa chọn "tự học có hướng dẫn" ban đầu.* |
| Đầu ra mỗi buổi | Bài giảng chi tiết · Instructor notes · Bài tập + lời giải · Slide outline + cheat sheet |
| Ngôn ngữ | Tiếng Việt có dấu; thuật ngữ kỹ thuật giữ tiếng Anh |
| Phạm vi | 5 trục + on-ramp; chọn lọc notebook theo trục (xem §10) |
| Cấu trúc | 5 trục vấn đề, eval-first (thay 10 module theo năng lực) |
| Định dạng đầu ra | **HTML custom = trang syllabus/landing**; **17 buổi chi tiết = MkDocs Material → GitHub Pages** |
| Repo | Standalone `claude-cookbooks-course` dưới `github.com/mduongvandinh` (thư mục dev tách biệt) |

**Ràng buộc kỹ thuật:**
- Notebook gốc không sửa/không copy; tham chiếu qua link Colab.
- Model ID hands-on dùng alias hiện tại: `claude-opus-4-8`, `claude-sonnet-5`, `claude-haiku-4-5`.
- File HTML/Markdown lưu **UTF-8 chuẩn** (bản HTML hiện tại đang double-encode/mojibake — phải sửa trước khi publish).
- Con số trong "bài phá trước" là kết quả điển hình để đối chiếu, **không phải hằng số** — mỗi lớp tự đo lại trên corpus của mình.

## 3. Bốn quy tắc sư phạm (xương sống, bắt buộc mọi buổi)

1. **Dự đoán trước, chạy sau.** Học viên viết dự đoán và khoá lại trước khi xem kết quả. Widget
   `predict-reveal` khoá ô kết quả tới khi có dự đoán (đã hiện thực trong HTML syllabus).
2. **Bắt đầu bằng cái hỏng.** Mỗi trục mở màn bằng một pipeline đã cấy lỗi (bài phá trước), không phải
   sample chạy đúng.
3. **Bánh cóc — chỉ quay một chiều.** Câu hỏi instructor trả lời chưa trôi → vào bộ câu hỏi vàng, ở lại
   tới khi có câu trả lời viết ra. Lỗi học viên từng gặp → test case vĩnh viễn.
4. **Vấn đề trước, công cụ sau.** Không buổi nào mang tên sản phẩm. Mỗi công cụ phải qua "thẻ biện minh":
   thay bằng gì vẫn chạy? gỡ ra thì chỉ số nào tụt? Không qua → cắt.

## 4. Kiến trúc 5 trục + on-ramp

**Buổi 0 · On-ramp (MỚI — xử lý lỗ hổng người mới).** Trước tuần 1, cho lớp hỗn hợp một buổi nền tảng để
người mới không rơi tự do ở trục 00: gọi Messages API, một prompt có cấu trúc, structured output, **một vòng
tool use**. Nguồn: `misc/how_to_enable_json_mode`, `tool_use/calculator_tool`, `tool_use/extracting_structured_json`.
Đây là prerequisite, không tính vào 5 trục và không có cổng.

| Trục | Câu hỏi trung tâm | Buổi | Cổng |
|---|---|---|---|
| **00 · Đo lường** | Làm sao biết hệ thống tốt lên hay xấu đi mà không phải cảm tính? | 3 | Cổng 00 |
| **01 · Truy hồi** | Tại sao nó lấy sai tài liệu — và là lỗi truy hồi hay lỗi sinh? | 4 | Cổng 01 |
| **02 · Sinh** | Context đã đúng, vì sao vẫn bịa — và dạy nó nói "không biết" thế nào? | 3 | Cổng 02 |
| **03 · Vòng lặp** | Khi nào cần agent thay vì pipeline tất định — chứng minh, không cảm thấy? | 4 | Cổng 03 |
| **04 · Vận hành** | Nó hỏng thế nào lúc 2 giờ sáng, và bạn biết sau bao lâu? | 3 | Cổng 04 · Tốt nghiệp |

Học viên chỉ qua trục sau khi vượt cổng của trục trước.

## 5. Corpus dùng chung + action layer

**Một corpus duy nhất** cho cả khoá: kho tài liệu kỹ thuật của một sản phẩm phần mềm (API docs, release notes,
bảng mã lỗi, config reference, migration guide). Vì sao: có phiên bản (sinh ra lệch thời gian), có mã lỗi/tên hàm
(chứng minh embedding thua keyword), có mâu thuẫn thật, có cấu trúc phân cấp, kiểm chứng được. Học viên tự thu
thập corpus riêng ở buổi 0.1 và giữ nguyên tới hết khoá.

**Action layer (MỚI — xử lý lỗ hổng trục 03).** Corpus toàn text thì agent (trục 03) không có gì để *làm*.
Bổ sung một **lớp mock tool/API** lên corpus (ví dụ: tra cứu bản ghi, cập nhật trạng thái, mở ticket) để trục 03
có action surface thật, không chỉ RAG lặp lại. Chốt lớp này cùng lúc chốt corpus ở buổi 0.1.

## 6. Cổng (gates) — định lượng, phân tầng

Mỗi cổng có tiêu chí bằng số. **Phân tầng (MỚI — xử lý lỗ hổng cổng quá gắt):** mỗi cổng có ngưỡng
**"tối thiểu để đi tiếp"** và **"đạt chuẩn"**, kèm buổi remediation, để cổng không thành nút cổ chai cho lớp hỗn hợp.

- **Cổng 00:** bộ đề vàng ≥ 30 câu, đủ 6 loại (mỗi loại ≥ 3), giám khảo đạt Cohen κ ≥ 0.6 trên 50 mẫu giữ riêng,
  một lệnh CLI cho ra một con số, lặp 2 lần chênh < 2%.
- **Cổng 01:** recall@10 trên bộ đề vàng tăng ≥ 15 điểm so với baseline (có log trước/sau); bảng đóng góp mỗi kỹ
  thuật (điểm thêm / ms tốn); nêu được kỹ thuật nào thử mà *làm tệ đi*.
- **Cổng 02:** faithfulness ≥ 0.90 trên tập giữ riêng; từ chối đúng ≥ 80% nhóm ngoài phạm vi, từ chối nhầm ≤ 5%
  nhóm trong phạm vi; nộp một ca vẫn sai + giải thích nguyên nhân gốc.
- **Cổng 03:** chứng minh bằng số agent thắng (hoặc thua + giải thích) pipeline tất định trên ≥ 1 nhóm tác vụ;
  độ chính xác chọn công cụ ≥ 0.90; báo cáo pass^3 (không chỉ pass@3).
- **Cổng 04 · Tốt nghiệp:** mỗi truy vấn sinh vết chạy lần ngược được từ khiếu nại về lượt gọi trong < 2 phút;
  nêu được p50/p95/p99 + chi phí mỗi truy vấn; eval tự động chặn khi điểm tụt; nộp một tài liệu sự cố.

## 7. Bài phá trước (break-first) + predict-reveal

Mỗi trục mở màn bằng một pipeline hỏng chạy được, kèm widget dự đoán. **Cần sản xuất code hỏng thật cho cả 5 trục**
(HTML syllabus mới có phần dẫn + widget, chưa có code chạy). Widget đã có trong HTML; port sang MkDocs bằng cùng
cơ chế (textarea + nút khoá + reveal, min ~25 ký tự).

## 8. Cut lists (danh sách cắt tường minh)

Mỗi trục nêu rõ cắt gì và vì sao (đúng quy tắc ④). **Bổ sung cắt tường minh còn thiếu:**
- **Multimodal** (vision/chart/PDF — cookbook mạnh) **cắt** vì corpus toàn text; nêu rõ thay vì bỏ im lặng.
- Trục 00: cắt benchmark học thuật (SWE-bench…), RL/reward design, so sánh nền tảng eval thương mại.
- Trục 01: cắt ~27 kỹ thuật RAG còn lại (trùng ý / không phải nút thắt / đòi hạ tầng / chỉ có nghĩa ở quy mô lớn).
- Trục 03: cắt tutorial gắn nhà cung cấp, giao thức đa-agent, fine-tuning (chỉ giới thiệu).
- Cách nói trên lớp: không nói "phần này không quan trọng"; nói "quan trọng khi bạn ở hoàn cảnh X, và đây là cách nhận ra".

## 9. Bộ câu hỏi vàng + chấm học viên + đổi máy

- **30 câu hỏi vàng** cho instructor (ratchet checklist đã hiện thực trong HTML). Ngưỡng: 28/30 trước buổi dạy đầu.
- **Chấm học viên bằng cổng** (không bằng bài nộp cuối): Đạt (5/5 cổng) → Vững (5/5 + vấn đáp) → Dạy được (+ chữa
  pipeline hỏng của người khác trong 30 phút). Không chấm số kỹ thuật đã dùng.
- **Bài thi cuối "đổi máy":** hai học viên đổi repo, 30 phút tìm + mô tả 3 điểm yếu lớn nhất kèm số đo.

## 10. Nguồn đã lọc (3 kho) + pin + license

- **Bài thực hành — Kho RAG cookbook:** giữ 8/~35 → trục 01, 02. Vật liệu tốt nhất (notebook chạy được).
  Lấy 8 kỹ thuật ở bảng trục 01, viết lại dẫn nhập theo hướng chẩn đoán, thêm phiên bản hỏng.
- **Phụ tùng — Kho tutorial agent lên sản phẩm:** giữ ~6/28 → trục 03, 04. **PIN CHÍNH XÁC repo + KIỂM LICENSE
  trước khi đưa vào nội dung thu phí** (kho này dùng giấy phép phi thương mại tuỳ chỉnh — rủi ro nếu thương mại hoá).
- **Tài liệu đọc — Thư viện nguồn eval:** giữ ~26/440+ → trục 00, 03, 04. Ba nhánh: (A) phân tích lỗi & giám khảo
  (~14 nguồn: Hamel Husain, Shreya Shankar, Eugene Yan; + Cohen κ, sai số chuẩn); (B) eval agent & quan sát (~8);
  (C) bảo mật & công cụ (~4 + bộ công cụ).
- **Bổ sung (từ cookbook):** on-ramp dùng `misc/how_to_enable_json_mode`, `tool_use/calculator_tool`,
  `tool_use/extracting_structured_json`; hands-on cụ thể dùng alias model hiện tại.

## 11. Template một buổi (deliverables)

Mỗi buổi (17 buổi + on-ramp) là một thư mục MkDocs, 5 file:
- `bai-giang.md` — mục tiêu → khái niệm (tiếng Việt) → đi qua code kèm "vì sao" → box Core/Đi sâu → thẻ biện minh
  công cụ → bài phá trước (predict-reveal) → lỗi thường gặp → tóm tắt + link. Đầu trang có link Colab.
- `instructor-notes.md` — thời lượng, thông điệp chốt, câu hỏi gợi mở, điểm hay vấp, gợi ý demo, nạp câu hỏi vàng.
- `bai-tap.md` + `loi-giai.md` — bài phân bậc + bước hướng tới cổng; mở đầu bằng "Dự đoán trước"; rubric.
- `slide-outline.md` — 8–12 slide + cheat sheet 1 trang.

## 12. Định dạng & tổ chức site

- **Trang syllabus (landing):** HTML custom "Giáo trình 5 trục" hiện tại (sau khi sửa encoding + các điểm §2–§10).
  Đây là bản đồ khoá + 4 quy tắc + bảng 5 trục + cổng + ratchet + đổi máy + lịch. Giữ nguyên phong cách thiết kế.
- **Nội dung 17 buổi:** MkDocs Material → GitHub Pages (dễ bảo trì). Trang syllabus HTML nhúng/liên kết vào site,
  hoặc đặt làm `index` tuỳ chọn tích hợp (chốt ở plan).
- Widget predict-reveal port sang MkDocs; cấu hình theme + extensions như bản plan trước.

## 13. Lịch chạy (giãn để hết lệch — xử lý lỗ hổng lịch)

9 tuần × 2 buổi = 18 slot, nhưng 17 buổi nội dung + buổi chấm cổng + "đổi máy" → tuần cuối bị nhồi 3 buổi.
**Chốt: giãn thành 10 tuần** (hoặc trộn "đổi máy" vào buổi 4.3). Tuần 2 và tuần 6 giữ buổi đệm vì hai cổng đầu
là nơi lớp tắc nhiều nhất. Nếu phải cắt: cắt trục 03 xuống 3 buổi, **không bao giờ cắt trục 00**.

## 14. Định nghĩa "đạt" cho tài liệu

- Mọi code hands-on chạy được, đối chiếu notebook gốc; model ID alias hiện tại.
- Mọi công cụ qua thẻ biện minh; mọi trục có cut list tường minh.
- Site MkDocs build `--strict` không lỗi; link nội bộ sống; widget predict-reveal khoá/mở đúng.
- HTML syllabus render tiếng Việt đúng (UTF-8, không mojibake); ratchet + predict-reveal chạy.
- Mỗi cổng có bài kiểm chứng bằng số + có ngưỡng phân tầng.

## 15. Phạm vi bản đầu (MVP pilot)

- **Sửa trang syllabus HTML:** encoding UTF-8; thêm Buổi 0 on-ramp; thêm cut Multimodal tường minh; giãn lịch
  10 tuần; thêm action layer vào phần corpus; cổng phân tầng.
- **Scaffold repo MkDocs** (mkdocs.yml, predict-reveal, CSS, deploy Pages) + nhúng syllabus.
- **Pilot Trục 00 (Đo lường) đầy đủ:** on-ramp Buổi 0 + 3 buổi (0.1 phân tích lỗi, 0.2 bộ đề vàng 6 loại,
  0.3 giám khảo & calibration) — mỗi buổi 5 file + bài phá trước "giám khảo hỏng" + Cổng 00 (phân tầng).
- Lý do chọn Trục 00 làm pilot: nó đi trước và gate mọi trục sau; validate được phần khó/mới nhất trước.

## 16. Ngoài phạm vi (YAGNI)

- Không viết đủ cả 5 trục ngay — chỉ pilot on-ramp + Trục 00.
- Không sửa/di chuyển notebook gốc.
- Không dựng backend/đăng nhập/chấm tự động online (cổng chấm thủ công theo số).
- Không làm Multimodal, fine-tuning, đa-agent (đã cắt tường minh).
- Không thương mại hoá nội dung từ kho license phi thương mại cho tới khi kiểm license xong.
