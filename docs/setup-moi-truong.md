# Cài đặt môi trường

## Lấy API key

Đăng ký và tạo key tại [console.anthropic.com](https://console.anthropic.com). Đặt vào biến môi trường:

```bash
export ANTHROPIC_API_KEY="sk-ant-..."
```

!!! danger "Không commit API key"
    Không bao giờ đưa API key vào code hay commit lên Git. Luôn đọc từ biến môi trường.

## Cài SDK

```bash
pip install anthropic
```

Client tự đọc `ANTHROPIC_API_KEY` từ môi trường:

```python
from anthropic import Anthropic
client = Anthropic()
```

## Chạy notebook nguồn

Mỗi buổi có nút **"Open in Colab"** trỏ tới notebook gốc trong repo Anthropic. Trên Colab, đặt
`ANTHROPIC_API_KEY` trong phần Secrets trước khi chạy.

## Model ID dùng trong giáo trình

!!! warning "Notebook nguồn có thể hiển thị model ID cũ"
    Một số notebook gốc còn dùng ID cũ như `claude-opus-4-1` hay `claude-sonnet-4-6`. Giáo trình này luôn
    dùng **alias hiện tại**:

    | Dòng | Alias |
    |---|---|
    | Opus | `claude-opus-4-8` |
    | Sonnet | `claude-sonnet-5` |
    | Haiku | `claude-haiku-4-5` |

    Model tiến hoá liên tục — luôn tra alias mới nhất tại [docs.claude.com](https://docs.claude.com), đừng
    hardcode ID có ngày. Chi tiết: [Model ID](cheat-sheets/model-ids.md).
