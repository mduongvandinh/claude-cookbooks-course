# Giáo trình 5 trục — On-ramp + Trục 00 Pilot Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Dựng repo standalone `claude-cookbooks-course` với trang syllabus HTML "5 trục" (đã sửa) làm landing, site MkDocs Material cho nội dung bài, và hoàn thiện **On-ramp Buổi 0 + Trục 00 (Đo lường)** làm pilot theo 4 quy tắc sư phạm + Cổng 00 phân tầng.

**Architecture:** Trang syllabus giữ nguyên HTML custom của người dùng (sửa UTF-8 + 6 điểm nội dung). Nội dung 17 buổi viết Markdown → MkDocs Material → GitHub Pages. Widget "dự đoán trước, chạy sau" port từ HTML sang JS thuần trong MkDocs. Code eval lấy cơ chế từ `building_evals`/`generate_test_cases`; phần pairwise-judge/position-bias/Cohen κ viết từ đầu (cookbook không có).

**Tech Stack:** MkDocs Material, Python venv, PyMdown Extensions, vanilla JS, GitHub Actions.

**Spec:** `docs/superpowers/specs/2026-07-24-giao-trinh-claude-cookbooks-design.md` (bản 5 trục)
**Thay thế:** plan cũ `2026-07-24-giao-trinh-module-1-pilot.md` (10-module) — đã lỗi thời, không dùng.

**Thư mục làm việc (repo mới, TÁCH BIỆT):**
`/Users/duongvandinh/Documents/2.Learn/AI/1.gh/mduongvandinh/claude-cookbooks-course` — gọi tắt `$COURSE`.

**Quy ước bắt buộc:**
- Tiếng Việt có dấu; thuật ngữ kỹ thuật giữ tiếng Anh; commit message tiếng Việt CÓ DẤU (chỉ tên file không dấu).
- Model ID mọi ví dụ: `claude-opus-4-8`, `claude-sonnet-5`, `claude-haiku-4-5`. Không ID cũ/có ngày.
- Notebook gốc không sửa/không copy; tham chiếu qua link Colab.
- Mọi file lưu UTF-8 chuẩn (không mojibake).
- "Test" của docs = `mkdocs build --strict` không lỗi + kiểm tra thủ công widget/UTF-8/link.

---

## File Structure

```
$COURSE/
  README.md
  .gitignore
  requirements.txt
  mkdocs.yml
  .github/workflows/deploy-docs.yml
  docs/
    index.md                          # landing MkDocs: dẫn vào syllabus + lộ trình
    syllabus.html                     # trang 5 trục HTML custom (đã sửa UTF-8 + 6 điểm)
    huong-dan-giang-vien.md
    setup-moi-truong.md
    so-loi-test-case.md               # ratchet lỗi (quy tắc ③)
    assets/
      stylesheets/extra.css
      javascripts/predict-reveal.js   # widget dự đoán (quy tắc ①)
      broken/
        giam_khao_hong.py             # bài phá trước Trục 00 (pairwise + position bias)
    cheat-sheets/
      eval-harness.md                 # grader prompt, % score, Cohen κ
      model-ids.md
    on-ramp/
      index.md
      buoi-0-nen-tang/                # 5 file: API, prompt, structured output, 1 vòng tool use
    truc-00-do-luong/
      index.md                        # tổng quan trục + câu hỏi trung tâm + cổng
      00-ca-hong.md                   # bài phá trước "giám khảo hỏng"
      bo-cau-hoi-vang.md              # ratchet câu hỏi (6 câu seed từ HTML)
      0.1-phan-tich-loi/              # 5 file
      0.2-bo-de-vang/                 # 5 file
      0.3-giam-khao-can-chinh/        # 5 file
      cong-00.md                      # tiêu chí Cổng 00 phân tầng
    phu-luc/index.md
```

---

## PHASE A — Trang syllabus HTML (sửa UTF-8 + 6 điểm nội dung)

### Task 1: Khởi tạo repo + đưa syllabus HTML vào (UTF-8)

**Files:**
- Create: `$COURSE/.gitignore`, `$COURSE/README.md`
- Create: `$COURSE/docs/syllabus.html`

- [ ] **Step 1: Tạo thư mục + git init**

```bash
mkdir -p "/Users/duongvandinh/Documents/2.Learn/AI/1.gh/mduongvandinh/claude-cookbooks-course/docs"
cd "/Users/duongvandinh/Documents/2.Learn/AI/1.gh/mduongvandinh/claude-cookbooks-course"
git init
```

- [ ] **Step 2: BƯỚC THỦ CÔNG của người dùng — export artifact ra UTF-8**

Người dùng mở artifact "Giáo trình 5 trục" trên claude.ai, chọn tải/xuất file HTML, lưu thành
`$COURSE/docs/syllabus.html`. Yêu cầu: file phải là **UTF-8 chuẩn** (không double-encode). Nếu người
dùng dán nội dung, executor lưu lại bằng công cụ Write (đảm bảo UTF-8), KHÔNG qua shell echo/redirect.

- [ ] **Step 3: Kiểm tra encoding**

Run: `file "$COURSE/docs/syllabus.html" && grep -c "Giáo trình" "$COURSE/docs/syllabus.html"`
Expected: `file` báo "UTF-8 Unicode text"; grep tìm thấy "Giáo trình" có dấu (≥ 1). Nếu grep = 0 hoặc thấy
"GiÃ¡o trÃ¬nh" → file đang mojibake, phải xuất lại đúng UTF-8 trước khi tiếp.

- [ ] **Step 4: `.gitignore` + `README.md`**

`.gitignore`:
```gitignore
site/
.venv/
__pycache__/
*.pyc
.DS_Store
```

`README.md`:
```markdown
# Claude Cookbooks Course — Giáo trình 5 trục

Bootcamp 10 tuần xây ứng dụng LLM sản xuất, tổ chức theo 5 trục vấn đề, eval-first.
Trang syllabus: `docs/syllabus.html`. Nội dung bài: site MkDocs (`mkdocs serve`).

Site: https://mduongvandinh.github.io/claude-cookbooks-course/
```

- [ ] **Step 5: Commit**

```bash
git add .gitignore README.md docs/syllabus.html
git commit -m "chore: khởi tạo repo + trang syllabus 5 trục (UTF-8)"
```

### Task 2: Sửa 6 điểm nội dung trong syllabus HTML

**Files:** Modify `$COURSE/docs/syllabus.html`

Áp dụng 6 chỉnh sửa (dùng Edit trên file UTF-8). Mỗi bước nêu rõ chèn/sửa gì.

- [ ] **Step 1: Thêm Buổi 0 on-ramp** — trong `<table class="tbl">` của mục "Bản đồ 5 trục", thêm một dòng
  TRƯỚC dòng "00 · Đo lường":
  ```html
  <tr><td>0 · Nền tảng</td><td>Gọi API, prompt, structured output, một vòng tool use (on-ramp cho người mới)</td><td class="num">1</td></tr>
  ```
  Và thêm một đoạn `<p>` dưới `.sub` của mục đó: "Buổi 0 là on-ramp cho lớp hỗn hợp trình độ — người mới học
  cơ chế gọi API/prompt/tool trước khi vào trục 00. Không có cổng, là prerequisite."

- [ ] **Step 2: Cắt Multimodal tường minh** — thêm một `<div class="cut">` mới trong mục "Bản đồ 5 trục" (sau
  phần corpus), nội dung:
  ```html
  <div class="cut"><h4>Cắt khỏi toàn khoá</h4>
  <ul><li><strong>Multimodal (vision, đọc chart, PDF)</strong> — cookbook mạnh phần này nhưng corpus toàn text,
  nên cắt tường minh theo quy tắc ④. Đưa vào phụ lục tuỳ chọn nếu học viên có nhu cầu ảnh/tài liệu quét.</li></ul></div>
  ```

- [ ] **Step 3: Thêm action layer vào corpus** — trong `.card` "Vì sao corpus này", thêm một `<li>`:
  ```html
  <li><strong>Có lớp hành động</strong> — kèm vài mock tool/API (tra bản ghi, cập nhật trạng thái, mở ticket) để trục 03 có action surface thật, không chỉ đọc tài liệu.</li>
  ```

- [ ] **Step 4: Cổng phân tầng** — trong mỗi `.gate-in`, thêm một `<p>` mở đầu:
  ```html
  <p><em>Hai ngưỡng: "tối thiểu để đi tiếp" (đủ vượt cổng) và "đạt chuẩn" (mức Vững). Lớp hỗn hợp có buổi remediation nếu chưa đạt tối thiểu.</em></p>
  ```

- [ ] **Step 5: Giãn lịch 10 tuần** — trong `<table>` mục "Lịch chạy", tách tuần 9 (đang có 3 buổi
  "4.2 · 4.3 · Đổi máy") thành:
  ```html
  <tr><td>9</td><td>4.2 Độ trễ &amp; chi phí · 4.3 Bảo mật</td><td class="num">—</td></tr>
  <tr><td>10</td><td>Đổi máy · Chấm Cổng 04</td><td class="num">Cổng 04</td></tr>
  ```
  Và sửa `<h2>` mục đó thành "Mười tuần, hai buổi mỗi tuần", cùng eyebrow "17 buổi · 10 tuần" ở hero.

- [ ] **Step 6: Sửa tiêu đề trục 00** — trong `.axis-meta` của trục 00, giữ "3 buổi" nhưng ghi chú Buổi 0 đứng
  trước: thêm `<br><span style="color:var(--gate)">+ Buổi 0 on-ramp</span>`.

- [ ] **Step 7: Kiểm tra + commit**

Run: `grep -c "Buổi 0" "$COURSE/docs/syllabus.html"` → Expected: ≥ 2. Mở file trong trình duyệt, xác nhận
tiếng Việt đúng, không mojibake, widget predict-reveal + ratchet vẫn chạy.

```bash
git add docs/syllabus.html
git commit -m "feat: sửa syllabus — on-ramp, cắt multimodal, action layer, cổng phân tầng, lịch 10 tuần"
```

---

## PHASE B — Scaffold MkDocs

### Task 3: Dependencies + venv + mkdocs.yml + landing

**Files:**
- Create: `$COURSE/requirements.txt`, `$COURSE/mkdocs.yml`, `$COURSE/docs/index.md`

- [ ] **Step 1: `requirements.txt`**

```
mkdocs-material>=9.5
pymdown-extensions>=10.7
```

- [ ] **Step 2: venv + cài + kiểm tra**

```bash
cd "/Users/duongvandinh/Documents/2.Learn/AI/1.gh/mduongvandinh/claude-cookbooks-course"
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs --version
```
Expected: in ra version mkdocs.

- [ ] **Step 3: `mkdocs.yml`**

```yaml
site_name: Claude Cookbooks Course
site_description: Giáo trình 5 trục — xây ứng dụng LLM sản xuất
site_url: https://mduongvandinh.github.io/claude-cookbooks-course/
repo_url: https://github.com/mduongvandinh/claude-cookbooks-course
theme:
  name: material
  language: vi
  features: [navigation.sections, navigation.top, content.code.copy, content.tabs.link, search.highlight]
  palette:
    - scheme: default
      primary: teal
      toggle: {icon: material/weather-night, name: Nền tối}
    - scheme: slate
      primary: teal
      toggle: {icon: material/weather-sunny, name: Nền sáng}
markdown_extensions:
  - admonition
  - attr_list
  - md_in_html
  - toc: {permalink: true}
  - pymdownx.details
  - pymdownx.superfences
  - pymdownx.highlight: {anchor_linenums: true}
  - pymdownx.tabbed: {alternate_style: true}
extra_css: [assets/stylesheets/extra.css]
extra_javascript: [assets/javascripts/predict-reveal.js]
nav:
  - Trang chủ: index.md
  - "Syllabus 5 trục": syllabus.html
  - Hướng dẫn giảng viên: huong-dan-giang-vien.md
  - Cài đặt môi trường: setup-moi-truong.md
  - "Buổi 0 — Nền tảng":
      - Tổng quan: on-ramp/index.md
      - "Nền tảng API & tool use": on-ramp/buoi-0-nen-tang/bai-giang.md
  - "Trục 00 — Đo lường":
      - Tổng quan: truc-00-do-luong/index.md
      - "Ca hỏng: giám khảo hỏng": truc-00-do-luong/00-ca-hong.md
      - "0.1 Phân tích lỗi": truc-00-do-luong/0.1-phan-tich-loi/bai-giang.md
      - "0.2 Bộ đề vàng": truc-00-do-luong/0.2-bo-de-vang/bai-giang.md
      - "0.3 Giám khảo & căn chỉnh": truc-00-do-luong/0.3-giam-khao-can-chinh/bai-giang.md
      - "Bộ câu hỏi vàng": truc-00-do-luong/bo-cau-hoi-vang.md
      - "Cổng 00": truc-00-do-luong/cong-00.md
  - Cheat sheets:
      - Eval harness: cheat-sheets/eval-harness.md
      - Model ID: cheat-sheets/model-ids.md
  - Sổ lỗi & test case: so-loi-test-case.md
  - Phụ lục: phu-luc/index.md
```

- [ ] **Step 4: `docs/index.md`** — landing MkDocs, nội dung bắt buộc: (1) `# Giáo trình 5 trục`; (2) đoạn
  giới thiệu eval-first, 5 trục, cohort 10 tuần; (3) link nổi bật tới `syllabus.html` ("Xem bản đồ 5 trục đầy đủ");
  (4) "## Bắt đầu" → link `setup-moi-truong.md` → `on-ramp/index.md`; (5) một khối `.predict` demo.

- [ ] **Step 5: Build (không strict vì nhiều file chưa có) + commit**

```bash
source .venv/bin/activate && mkdocs build 2>&1 | tail -5
git add requirements.txt mkdocs.yml docs/index.md
git commit -m "feat: scaffold mkdocs material + nav 5 trục"
```

### Task 4: Widget predict-reveal + CSS

**Files:** Create `$COURSE/docs/assets/javascripts/predict-reveal.js`, `$COURSE/docs/assets/stylesheets/extra.css`

- [ ] **Step 1: `predict-reveal.js`** (min 25 ký tự, khớp hành vi HTML syllabus)

```javascript
// Widget "Dự đoán trước, chạy sau" (quy tắc ①). Ô .predict-result ẩn tới khi gõ dự đoán >= 25 ký tự.
document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll(".predict").forEach(function (box, i) {
    var input = box.querySelector(".predict-input");
    var btn = box.querySelector(".predict-btn");
    var result = box.querySelector(".predict-result");
    if (!input || !btn || !result) return;
    var key = "predict:" + window.location.pathname + ":" + i;
    var MIN = 25;
    function reveal() {
      input.setAttribute("disabled", "disabled");
      btn.setAttribute("disabled", "disabled");
      btn.textContent = "Đã khoá — đối chiếu bên dưới";
      result.hidden = false;
      box.classList.add("revealed");
    }
    var saved = null;
    try { saved = window.localStorage.getItem(key); } catch (e) {}
    if (saved) { input.value = saved; reveal(); }
    input.addEventListener("input", function () {
      btn.disabled = input.value.trim().length < MIN;
    });
    btn.disabled = true;
    btn.addEventListener("click", function () {
      if (input.value.trim().length < MIN) return;
      try { window.localStorage.setItem(key, input.value.trim()); } catch (e) {}
      reveal();
    });
  });
});
```

- [ ] **Step 2: `extra.css`** — style `.predict`, `.predict-input`, `.predict-btn`, `.predict-result`,
  `.tool-justify` (thẻ biện minh công cụ). Dùng biến màu Material (`--md-primary-fg-color`,
  `--md-code-bg-color`). Tối thiểu: viền trái nhấn màu, input full-width min-height 3.5rem, nút primary,
  `.predict-result` khi ẩn dùng thuộc tính `hidden`.

- [ ] **Step 3: Thêm widget demo vào `docs/index.md`** (khối `.predict` với `<textarea class="predict-input">`,
  `<button class="predict-btn">`, `<div class="predict-result" hidden markdown>`), rồi `mkdocs serve` kiểm tra
  khoá/mở đúng.

- [ ] **Step 4: Commit**

```bash
git add docs/assets docs/index.md
git commit -m "feat: widget predict-reveal + css (quy tắc 1)"
```

### Task 5: Trang khung — hướng dẫn giảng viên, setup, sổ lỗi, cheat sheets, phụ lục

**Files:** Create `huong-dan-giang-vien.md`, `setup-moi-truong.md`, `so-loi-test-case.md`,
`cheat-sheets/eval-harness.md`, `cheat-sheets/model-ids.md`, `phu-luc/index.md`

- [ ] **Step 1: `huong-dan-giang-vien.md`** — bắt buộc: 4 quy tắc sư phạm đầy đủ; giải thích cấu trúc 5 file/buổi;
  giải thích cơ chế cổng phân tầng + đổi máy; checklist chuẩn bị (đạt 28/30 câu hỏi vàng, chạy thử notebook Colab,
  chốt corpus + action layer ở buổi 0.1).

- [ ] **Step 2: `setup-moi-truong.md`** — bắt buộc: lấy API key (`export ANTHROPIC_API_KEY=...`, cảnh báo không
  commit); `pip install anthropic`; chạy notebook Colab; admonition cảnh báo model ID cũ trong notebook
  (`claude-opus-4-1`, `claude-sonnet-4-6`) → giáo trình dùng alias hiện tại; link `cheat-sheets/model-ids.md`.

- [ ] **Step 3: `cheat-sheets/eval-harness.md`** — chứa code chuẩn (dùng nguyên):

```python
from anthropic import Anthropic
import re
from collections import Counter
client = Anthropic()
MODEL_NAME = "claude-sonnet-5"

def get_completion(messages, max_tokens=2048):
    return client.messages.create(model=MODEL_NAME, max_tokens=max_tokens, messages=messages).content[0].text

# --- Chấm bằng model (single-output, rubric) — mẫu từ building_evals ---
def build_grader_prompt(answer, rubric):
    content = (
        "Bạn được cho một câu trả lời và một rubric.\n"
        f"<answer>{answer}</answer>\n<rubric>{rubric}</rubric>\n"
        "Suy nghĩ trong <thinking></thinking>. Sau đó xuất 'correct' hoặc 'incorrect' trong <correctness></correctness>."
    )
    return [{"role": "user", "content": content}]

def grade(output, rubric):
    completion = get_completion(build_grader_prompt(output, rubric))
    m = re.search(r"<correctness>(.*?)</correctness>", completion, re.DOTALL)
    if not m:
        raise ValueError("Không tìm thấy thẻ <correctness>")
    return m.group(1).strip()

# --- Cohen kappa (stdlib thuần) — đo đồng thuận giám khảo vs người ---
def cohen_kappa(a, b):
    n = len(a)
    po = sum(1 for x, y in zip(a, b) if x == y) / n
    ca, cb = Counter(a), Counter(b)
    pe = sum((ca[k] / n) * (cb[k] / n) for k in set(a) | set(b))
    return 1.0 if pe == 1 else (po - pe) / (1 - pe)
```

- [ ] **Step 4: `cheat-sheets/model-ids.md`** — bảng Opus `claude-opus-4-8` / Sonnet `claude-sonnet-5` /
  Haiku `claude-haiku-4-5` + ghi chú notebook nguồn có ID cũ.

- [ ] **Step 5: `so-loi-test-case.md`** — giải thích quy tắc ③ cho học viên; bảng "Lỗi | Nguyên nhân | Test case"
  seed 1 dòng từ ca hỏng Trục 00 (position bias: đo A vs B mà không hoán đổi vị trí).

- [ ] **Step 6: `phu-luc/index.md`** — danh mục notebook tham khảo ngoài mạch chính (Multimodal đã cắt, Managed
  Agents, Skills, third-party...) với link Colab; ghi rõ tuỳ chọn mở rộng.

- [ ] **Step 7: Build strict + commit**

```bash
source .venv/bin/activate && mkdocs build --strict 2>&1 | tail -10
git add docs/huong-dan-giang-vien.md docs/setup-moi-truong.md docs/so-loi-test-case.md docs/cheat-sheets docs/phu-luc
git commit -m "feat: trang khung — hướng dẫn giảng viên, setup, cheat sheet eval, phụ lục"
```

---

## PHASE C — On-ramp Buổi 0

### Task 6: Buổi 0 — nền tảng API & tool use

**Files:** Create `on-ramp/index.md` + `on-ramp/buoi-0-nen-tang/` (5 file: `bai-giang.md`, `instructor-notes.md`,
`bai-tap.md`, `loi-giai.md`, `slide-outline.md`)

**Code nguồn (chuẩn hoá model `claude-sonnet-5`):**
```python
from anthropic import Anthropic
client = Anthropic()
MODEL_NAME = "claude-sonnet-5"

# (a) Gọi API cơ bản
msg = client.messages.create(model=MODEL_NAME, max_tokens=1024,
    messages=[{"role": "user", "content": "Tóm tắt đoạn sau trong 1 câu: ..."}])

# (b) Một vòng tool use (từ calculator_tool)
tools = [{"name": "calculator", "description": "Thực hiện phép tính số học.",
    "input_schema": {"type": "object", "properties": {"expression": {"type": "string"}}, "required": ["expression"]}}]
r = client.messages.create(model=MODEL_NAME, max_tokens=1024, tools=tools,
    messages=[{"role": "user", "content": "Tính 1984135 * 9343116"}])
if r.stop_reason == "tool_use":
    tu = next(b for b in r.content if b.type == "tool_use")
    result = str(eval(tu.input["expression"]))  # demo, eval KHÔNG an toàn production
    r2 = client.messages.create(model=MODEL_NAME, max_tokens=1024, tools=tools, messages=[
        {"role": "user", "content": "Tính 1984135 * 9343116"},
        {"role": "assistant", "content": r.content},
        {"role": "user", "content": [{"type": "tool_result", "tool_use_id": tu.id, "content": result}]}])

# (c) Structured output bằng tool (từ extracting_structured_json)
tools2 = [{"name": "print_sentiment_scores", "description": "In điểm cảm xúc.",
    "input_schema": {"type": "object", "properties": {
        "positive": {"type": "number"}, "negative": {"type": "number"}, "neutral": {"type": "number"}},
        "required": ["positive", "negative", "neutral"]}}]
r3 = client.messages.create(model=MODEL_NAME, max_tokens=1024, tools=tools2,
    tool_choice={"type": "tool", "name": "print_sentiment_scores"},
    messages=[{"role": "user", "content": "Sản phẩm này tuyệt vời!"}])
scores = next(b.input for b in r3.content if b.type == "tool_use")
```

- [ ] **Step 1: `on-ramp/index.md`** — mục tiêu on-ramp, ai cần học (người mới), 3 kỹ năng: gọi API, một vòng
  tool use, structured output; link Colab `calculator_tool`, `extracting_structured_json`, `how_to_enable_json_mode`.

- [ ] **Step 2: `bai-giang.md`** theo template: tiêu đề `# Buổi 0 — Nền tảng: gọi được Claude và một vòng tool use`;
  mục tiêu; `.predict` ("Claude không tự tính số lớn chính xác — dự đoán nó trả về đáp số hay yêu cầu gọi tool?");
  đi qua 3 khối code (a)(b)(c) kèm "vì sao"; `.tool-justify` cho tool calculator; `??? note "Đi sâu"` về `eval()`
  không an toàn + `tool_choice`; lỗi thường gặp (quên `tool_use_id`, sai `stop_reason`); tóm tắt + link Trục 00.

- [ ] **Step 3–5:** `instructor-notes.md` (thời lượng ~90 phút vì lớp hỗn hợp; điểm người mới hay vấp), `bai-tap.md`
  (Core: thêm phép chia + chặn chia 0; Đi sâu: structured output cho một field lồng nhau — "Dự đoán trước"),
  `loi-giai.md` (code đầy đủ + rubric), `slide-outline.md` (8–10 slide).

- [ ] **Step 6: Build strict + `mkdocs serve` kiểm tra widget + commit**

```bash
source .venv/bin/activate && mkdocs build --strict 2>&1 | tail -10
git add docs/on-ramp
git commit -m "feat(on-ramp): buổi 0 nền tảng API & tool use"
```

---

## PHASE D — Trục 00 (Đo lường)

### Task 7: Trục 00 — tổng quan + bộ câu hỏi vàng + Cổng 00

**Files:** Create `truc-00-do-luong/index.md`, `truc-00-do-luong/bo-cau-hoi-vang.md`, `truc-00-do-luong/cong-00.md`

- [ ] **Step 1: `index.md`** — câu hỏi trung tâm ("Làm sao biết hệ thống tốt lên hay xấu đi mà không phải cảm
  tính?"); vì sao trục này đi trước tất cả (điều kiện cần của 4 trục sau); bảng 3 buổi (0.1/0.2/0.3) + "vấn đề
  giải quyết"; nhắc chốt corpus + action layer ở buổi 0.1; link Colab `building_evals`, `generate_test_cases`.

- [ ] **Step 2: `bo-cau-hoi-vang.md`** — quy tắc ③; bảng "Câu hỏi | Trả lời (điền dần)" seed **6 câu Trục 00 lấy
  từ syllabus HTML** (giám khảo đồng ý 85% đủ chưa; vì sao nhãn nhị phân tốt hơn thang 1–5; sao không để model tự
  sinh 1000 test; bộ đề 30 câu có 28 câu dữ kiện vấn đề ở đâu; điểm eval tăng 4% sao biết không phải nhiễu; vì sao
  không viết xong tiêu chí chấm trước khi chấm) + đáp án ngắn cho mỗi câu.

- [ ] **Step 3: `cong-00.md`** — Cổng 00 phân tầng. Nêu rõ 3 điều kiện + 2 ngưỡng (tối thiểu/đạt chuẩn):
  - Bộ đề vàng: tối thiểu ≥ 24 câu / đạt chuẩn ≥ 30 câu, đủ 6 loại (mỗi loại ≥ 3).
  - Giám khảo: tối thiểu Cohen κ ≥ 0.4 / đạt chuẩn ≥ 0.6 trên 50 mẫu giữ riêng.
  - Một lệnh CLI ra một con số, lặp 2 lần chênh < 2%.
  - Ghi rõ: chưa đạt tối thiểu → buổi remediation, không sang Trục 01.

- [ ] **Step 4: Build strict + commit**

```bash
source .venv/bin/activate && mkdocs build --strict 2>&1 | tail -10
git add docs/truc-00-do-luong/index.md docs/truc-00-do-luong/bo-cau-hoi-vang.md docs/truc-00-do-luong/cong-00.md
git commit -m "feat(trục00): tổng quan + bộ câu hỏi vàng + cổng 00 phân tầng"
```

### Task 8: Bài phá trước — "giám khảo hỏng" (position bias)

**Files:** Create `$COURSE/docs/assets/broken/giam_khao_hong.py`, `truc-00-do-luong/00-ca-hong.md`

**Code (viết từ đầu — cookbook không có pairwise judge; đây là bản HỎNG chỉ chấm một chiều):**
```python
"""
CA HỎNG — Trục 00. Bộ chấm so cặp: đưa hai câu trả lời A và B, giám khảo (model) chọn cái tốt hơn.
Trên 200 cặp, A thắng 65%. Học viên kết luận "cấu hình A tốt hơn". NHIỆM VỤ: bản này sai ở đâu?
"""
from anthropic import Anthropic
import re
client = Anthropic()
MODEL_NAME = "claude-sonnet-5"

def judge_once(question, answer_first, answer_second):
    prompt = (
        f"Câu hỏi: {question}\n"
        f"Câu trả lời A: {answer_first}\n"
        f"Câu trả lời B: {answer_second}\n"
        "Câu nào tốt hơn? Chỉ xuất 'A' hoặc 'B' trong <winner></winner>."
    )
    out = client.messages.create(model=MODEL_NAME, max_tokens=256,
        messages=[{"role": "user", "content": prompt}]).content[0].text
    m = re.search(r"<winner>(.*?)</winner>", out, re.DOTALL)
    return m.group(1).strip()

def run(pairs):
    # LỖI: luôn đặt cấu hình A ở vị trí đầu, cấu hình B ở vị trí sau — không hoán đổi.
    wins_a = 0
    for q, ans_a, ans_b in pairs:
        if judge_once(q, ans_a, ans_b) == "A":
            wins_a += 1
    return wins_a / len(pairs)
```

- [ ] **Step 1: Viết `giam_khao_hong.py`** (nội dung trên).

- [ ] **Step 2: Viết `00-ca-hong.md`** — bắt buộc: `# Ca hỏng — Giám khảo hỏng`; bối cảnh (A thắng 65% trên 200
  cặp); nhúng code `giam_khao_hong.py`; `.predict` ("Bạn yêu cầu chạy lại đúng 200 cặp nhưng hoán đổi vị trí A và
  B. Dự đoán tỉ lệ thắng sẽ ra sao?"); trong `.predict-result`: giải thích **position bias** — tỉ lệ thắng của
  *vị trí thứ nhất* gần như không đổi (~60–65%) dù đã hoán nội dung; cái đo được là thiên lệch vị trí, không phải
  chất lượng A. Bản sửa: chạy cả hai chiều rồi lấy trung bình, hoặc chuyển sang chấm nhị phân từng câu. Kết bằng
  quy tắc ①/②; feed lỗi vào `so-loi-test-case.md`.

- [ ] **Step 3: Build strict + commit**

```bash
source .venv/bin/activate && mkdocs build --strict 2>&1 | tail -10
git add docs/assets/broken/giam_khao_hong.py docs/truc-00-do-luong/00-ca-hong.md
git commit -m "feat(trục00): ca hỏng giám khảo hỏng — position bias (quy tắc 2)"
```

### Task 9: Buổi 0.1 — Phân tích lỗi trước khi nghĩ tới chỉ số

**Files:** Create `truc-00-do-luong/0.1-phan-tich-loi/` (5 file)

- [ ] **Step 1: `bai-giang.md`** — tiêu đề `# 0.1 — Phân tích lỗi trước khi nghĩ tới chỉ số`; mục tiêu (đọc tay
  100 lượt tương tác, mã hoá mở → 6–8 nhóm lỗi, xếp theo ảnh hưởng); `.predict` ("Trước khi xây dashboard, đọc tay
  100 lượt — dự đoán bạn sẽ tìm được bao nhiêu *loại* lỗi khác nhau?"); phương pháp mã hoá mở (open coding) trên
  bảng tính, không công cụ; kết quả bắt buộc = danh sách nhóm lỗi có tần suất; chốt corpus + action layer; link
  nguồn ngoài (Hamel Husain error analysis). Ít code — chủ yếu quy trình.

- [ ] **Step 2–5:** `instructor-notes.md` (nhấn: đừng vội đo, đọc dữ liệu thật trước; nạp câu hỏi vàng "sao không
  để model tự sinh test?"), `bai-tap.md` (Core: mã hoá mở 30 lượt của corpus riêng → ≥ 5 nhóm lỗi; Đi sâu: xếp
  hạng nhóm theo ảnh hưởng × tần suất — "Dự đoán trước"), `loi-giai.md` (rubric: nhóm lỗi tách bạch, có tần suất),
  `slide-outline.md`.

- [ ] **Step 6: Build strict + commit**

```bash
source .venv/bin/activate && mkdocs build --strict 2>&1 | tail -10
git add docs/truc-00-do-luong/0.1-phan-tich-loi
git commit -m "feat(trục00): buổi 0.1 phân tích lỗi"
```

### Task 10: Buổi 0.2 — Bộ đề vàng và sáu loại câu hỏi

**Files:** Create `truc-00-do-luong/0.2-bo-de-vang/` (5 file)

**Code nguồn (sinh test case — pattern từ generate_test_cases, model `claude-sonnet-5`):**
```python
from anthropic import Anthropic
client = Anthropic()
MODEL_NAME = "claude-sonnet-5"

def sinh_cau_hoi(loai, tai_lieu, so_luong=3):
    prompt = (
        f"Từ tài liệu sau, sinh {so_luong} câu hỏi thuộc loại '{loai}'.\n"
        f"<tài liệu>{tai_lieu}</tài liệu>\n"
        "Mỗi câu hỏi trong một thẻ <q></q>."
    )
    out = client.messages.create(model=MODEL_NAME, max_tokens=1024, temperature=1,
        messages=[{"role": "user", "content": prompt}]).content[0].text
    import re
    return re.findall(r"<q>(.*?)</q>", out, re.DOTALL)

SAU_LOAI = ["dữ kiện", "thời gian/phiên bản", "biên", "ngoài phạm vi", "đối kháng", "nhất quán"]
```

- [ ] **Step 1: `bai-giang.md`** — tiêu đề `# 0.2 — Bộ đề vàng và sáu loại câu hỏi`; mục tiêu (6 loại; vì sao bộ
  đề toàn câu dữ kiện là vô dụng — nó không bao giờ trượt; tự sinh bằng model dùng ở đâu, hỏng ở đâu, vì sao vẫn
  cần người duyệt; tách tập giữ riêng); `.predict` ("Bộ đề 30 câu của bạn có 28 câu dữ kiện. Dự đoán: nó sẽ nói
  gì sai lệch về hệ thống của bạn?"); giải thích 6 loại kèm ví dụ trên corpus; khối code `sinh_cau_hoi`;
  `.tool-justify` cho "tự sinh bằng model" (thay bằng gì: viết tay; gỡ ra thì chỉ số nào tụt: độ phủ/tốc độ tạo đề);
  link Colab `generate_test_cases`.

- [ ] **Step 2–5:** `instructor-notes.md`, `bai-tap.md` (Core: sinh ≥ 3 câu mỗi loại cho corpus riêng, người duyệt;
  Đi sâu: tách tập giữ riêng 20% — "Dự đoán trước"), `loi-giai.md`, `slide-outline.md`.

- [ ] **Step 6: Build strict + commit**

```bash
source .venv/bin/activate && mkdocs build --strict 2>&1 | tail -10
git add docs/truc-00-do-luong/0.2-bo-de-vang
git commit -m "feat(trục00): buổi 0.2 bộ đề vàng 6 loại"
```

### Task 11: Buổi 0.3 — Bộ chấm và bài toán căn chỉnh

**Files:** Create `truc-00-do-luong/0.3-giam-khao-can-chinh/` (5 file)

**Code nguồn (grader từ building_evals + Cohen κ viết từ đầu, model `claude-sonnet-5`):** dùng lại `grade()` và
`cohen_kappa()` ở `cheat-sheets/eval-harness.md` (Task 5, Step 3). Bản sửa của ca hỏng (chạy hai chiều):
```python
def judge_pair_debiased(question, ans_a, ans_b):
    # Chạy cả hai chiều rồi tổng hợp — khử position bias
    from collections import Counter
    v1 = judge_once(question, ans_a, ans_b)          # A ở vị trí đầu
    v2 = judge_once(question, ans_b, ans_a)          # A ở vị trí sau
    # v2 == "B" nghĩa là chọn ans_a (vì ans_a giờ là "B")
    picks_a = (v1 == "A") + (v2 == "B")
    if picks_a == 2: return "A"
    if picks_a == 0: return "B"
    return "hoà"   # bất đồng giữa hai chiều = tín hiệu câu khó/giám khảo yếu
```

- [ ] **Step 1: `bai-giang.md`** — tiêu đề `# 0.3 — Bộ chấm và bài toán căn chỉnh`; mục tiêu (nhãn nhị phân vs
  thang 1–5; model làm giám khảo & các thiên lệch: vị trí, độ dài, tự ưu ái; căn chỉnh với *một* người chấm chuẩn,
  đo bằng Cohen κ chứ không "tỉ lệ đồng ý"; vì sao 85% đồng ý có thể tệ hơn tung đồng xu); nối lại ca hỏng Task 8 →
  đưa bản sửa `judge_pair_debiased`; khối `grade()` + `cohen_kappa()`; `.predict` ("Giám khảo đồng ý 85% với nhãn
  người. Dự đoán κ là bao nhiêu nếu 80% mẫu là nhãn 'correct'?"); `.tool-justify` cho "model làm giám khảo".

- [ ] **Step 2–5:** `instructor-notes.md`, `bai-tap.md` (Core: tính κ giữa giám khảo và nhãn tay trên 50 mẫu;
  Đi sâu: khử position bias bằng chạy hai chiều, so κ trước/sau — "Dự đoán trước"), `loi-giai.md` (code κ đầy đủ +
  rubric), `slide-outline.md`.

- [ ] **Step 6: Build strict + commit**

```bash
source .venv/bin/activate && mkdocs build --strict 2>&1 | tail -10
git add docs/truc-00-do-luong/0.3-giam-khao-can-chinh
git commit -m "feat(trục00): buổi 0.3 giám khảo & căn chỉnh (Cohen κ)"
```

---

## PHASE E — Deploy & kiểm thử cuối

### Task 12: GitHub Actions + kiểm thử toàn site

**Files:** Create `$COURSE/.github/workflows/deploy-docs.yml`

- [ ] **Step 1: `deploy-docs.yml`**

```yaml
name: Deploy docs to GitHub Pages
on:
  push:
    branches: [main]
permissions:
  contents: write
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: {python-version: "3.12"}
      - run: pip install -r requirements.txt
      - run: mkdocs gh-deploy --force
```

- [ ] **Step 2: Build strict cuối cùng**

Run: `source .venv/bin/activate && mkdocs build --strict 2>&1 | tail -20`
Expected: "Documentation built" không WARNING/ERROR; mọi file trong nav tồn tại.

- [ ] **Step 3: Kiểm thử thủ công (serve)** — duyệt: landing → syllabus.html (tiếng Việt đúng, không mojibake,
  ratchet + predict chạy) → Buổi 0 → Trục 00 (0.1/0.2/0.3, widget predict khoá/mở đúng) → Cổng 00. Không link 404.

- [ ] **Step 4: Commit + bước thủ công người dùng**

```bash
git add .github/workflows/deploy-docs.yml
git commit -m "ci: deploy mkdocs lên github pages"
git branch -M main
```

Bước thủ công của người dùng (không tự động hoá): tạo repo rỗng `claude-cookbooks-course` trên GitHub →
`git remote add origin` → `git push -u origin main` (chỉ khi người dùng đồng ý) → Settings → Pages → nhánh
`gh-pages` → chờ Action → mở `https://mduongvandinh.github.io/claude-cookbooks-course/`.

---

## Self-Review (đối chiếu spec 5 trục)

**Spec coverage:**
- §2 repo standalone + UTF-8 → Task 1 (git init, kiểm encoding), Task 12 (push thủ công). ✓
- §3 bốn quy tắc → ① Task 4 widget + dùng mọi buổi; ② Task 8 ca hỏng; ③ Task 5/7 sổ lỗi + câu hỏi vàng;
  ④ thẻ biện minh trong Task 6/10/11. ✓
- §4 on-ramp Buổi 0 → Task 6. Trục 00 (3 buổi) → Task 9/10/11. ✓
- §5 corpus + action layer → syllabus Task 2 Step 3 + nhắc chốt ở 0.1 (Task 9) và index (Task 7). ✓
- §6 cổng phân tầng → Task 7 Step 3 (cong-00.md) + syllabus Task 2 Step 4. ✓
- §7 break-first → Task 8. §8 cut Multimodal → syllabus Task 2 Step 2 + phụ lục Task 5. ✓
- §9 câu hỏi vàng ratchet → giữ trong syllabus.html + seed truc-00 Task 7. ✓
- §10 nguồn + license → setup/phụ lục; license note trong spec (không thu phí ở pilot). ✓
- §12 HTML syllabus + MkDocs → Phase A (HTML) + Phase B–E (MkDocs). ✓
- §13 lịch 10 tuần → syllabus Task 2 Step 5. ✓
- §14 định nghĩa đạt → gate `mkdocs build --strict` mọi task + Task 12 kiểm UTF-8/widget. ✓
- §15 MVP = on-ramp + Trục 00 → toàn plan đúng phạm vi. ✓

**Placeholder scan:** config/JS/CSS/code eval + code hỏng có nội dung đầy đủ; file teaching đặc tả theo mục bắt buộc
+ code nguồn chính xác. Không "viết nội dung phù hợp" chung chung. ✓

**Type/tên nhất quán:** `get_completion`, `grade`, `cohen_kappa`, `judge_once`, `judge_pair_debiased`, `MODEL_NAME`,
`.predict/.predict-input/.predict-btn/.predict-result` dùng nhất quán; đường dẫn thư mục khớp giữa `mkdocs.yml` nav
(Task 3) và task tạo file (6–11). ✓

**Ghi chú:** Phần lõi Trục 00 (pairwise judge, position bias, Cohen κ) KHÔNG có trong cookbook — plan viết từ đầu,
đúng chuẩn, stdlib thuần; cơ chế harness (grader + % score) và sinh đề bám `building_evals`/`generate_test_cases`.
```