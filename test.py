S = input()

b_cnt = 0
del_cnt = 0

for c in S:
    if c == "A":
        del_cnt = min(b_cnt, del_cnt + 1)
    else:
        b_cnt += 1

print(del_cnt)