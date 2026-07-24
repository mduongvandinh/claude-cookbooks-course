# Lời giải — Buổi 0.3

## Core — Tính κ

```python
# nhan_may: nhãn giám khảo; nhan_nguoi: nhãn tay — cùng độ dài, mỗi phần tử 'correct'/'incorrect'
nhan_may = [grade(o, r) for o, r in zip(outputs, rubrics)]
k = cohen_kappa(nhan_may, nhan_nguoi)
print(f"Tỉ lệ đồng ý: {sum(x==y for x,y in zip(nhan_may,nhan_nguoi))/len(nhan_may):.0%}")
print(f"Cohen κ: {k:.2f}")
```

Điểm mấu chốt: tỉ lệ đồng ý có thể 85% mà κ chỉ ~0.06 nếu tỉ lệ nền lệch. **Rubric:** ra κ đúng (2đ); giải
thích khoảng cách đồng-ý-vs-κ (1đ).

## Đi sâu — Khử position bias

Chạy `judge_pair_debiased` (hai chiều) thường **tăng** κ vì loại được nhiễu vị trí. **Rubric:** hai giá trị κ
(1đ); giải thích đúng chiều (2đ).

## Capstone — Giám khảo cho trợ lý

```python
# Một lệnh CLI: python cham.py  ->  in ra một con số (điểm faithfulness/đúng)
```

**Rubric:** κ ≥ 0.4 (2đ); một lệnh ra một con số (1đ); lặp 2 lần chênh < 2% (1đ).
