# Buổi 0 — Nền tảng (on-ramp)

Buổi này dành cho **người mới với Claude API**. Nếu bạn đã gọi API, viết prompt và định nghĩa tool thành thạo,
bạn có thể nhảy thẳng tới [Trục 00](../truc-00-do-luong/index.md). Nếu chưa, đây là đường vào để không bị rơi
tự do khi Trục 00 nói về giám khảo, Cohen κ và bộ đề vàng.

Buổi 0 **không có cổng** — nó là prerequisite, không phải một trục.

## Ba kỹ năng bạn sẽ có sau buổi này

| Kỹ năng | Vì sao cần cho phần sau |
|---|---|
| Gọi Messages API | Mọi eval, RAG, agent đều bắt đầu từ một lời gọi |
| Một vòng tool use | Trục 03 là tool use lặp nhiều bước — phải nắm một vòng trước |
| Structured output bằng tool | Trục 00/02 cần model trả về dữ liệu có cấu trúc để chấm |

## Notebook nguồn

- [calculator_tool](https://colab.research.google.com/github/anthropics/claude-cookbooks/blob/main/tool_use/calculator_tool.ipynb) — một vòng tool use
- [extracting_structured_json](https://colab.research.google.com/github/anthropics/claude-cookbooks/blob/main/tool_use/extracting_structured_json.ipynb) — structured output bằng tool
- [how_to_enable_json_mode](https://colab.research.google.com/github/anthropics/claude-cookbooks/blob/main/misc/how_to_enable_json_mode.ipynb) — JSON mode

**[→ Vào bài giảng](buoi-0-nen-tang/bai-giang.md)**
