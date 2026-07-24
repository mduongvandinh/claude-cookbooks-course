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
    out = client.messages.create(
        model=MODEL_NAME, max_tokens=256,
        messages=[{"role": "user", "content": prompt}],
    ).content[0].text
    m = re.search(r"<winner>(.*?)</winner>", out, re.DOTALL)
    return m.group(1).strip()


def run(pairs):
    # LỖI: luôn đặt cấu hình A ở vị trí đầu, cấu hình B ở vị trí sau — không hoán đổi.
    wins_a = 0
    for question, ans_a, ans_b in pairs:
        if judge_once(question, ans_a, ans_b) == "A":
            wins_a += 1
    return wins_a / len(pairs)
