# Model ID hiện tại

| Dòng | Alias hiện tại | Dùng khi |
|---|---|---|
| Opus | `claude-opus-4-8` | Tác vụ khó, suy luận sâu |
| Sonnet | `claude-sonnet-5` | Cân bằng, mặc định cho hầu hết bài |
| Haiku | `claude-haiku-4-5` | Nhanh/rẻ, tác vụ nhẹ, sub-agent |

!!! note "Luôn dùng alias không kèm ngày"
    Tra bản mới nhất tại [docs.claude.com](https://docs.claude.com). Notebook nguồn trong cookbook có thể còn
    ID cũ (`claude-opus-4-1`, `claude-sonnet-4-6`) — đó là một điểm dạy về việc model tiến hoá: đừng hardcode
    ID có ngày, luôn dùng alias mới nhất.
