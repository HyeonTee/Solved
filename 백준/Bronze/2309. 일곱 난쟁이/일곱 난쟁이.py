import sys
from itertools import combinations

height_list = [None] * 9
height_sum = 0

for i in range(9):
    height = int(sys.stdin.readline().strip())
    height_list[i] = height
    height_sum += height

height_over = height_sum - 100

comb_list = list(combinations(height_list,2))

for comb in comb_list:
    two_sum = sum(comb)
    if two_sum == height_over:
        ans_comb = comb
        break

height_list.remove(list(ans_comb)[0])
height_list.remove(list(ans_comb)[1])
height_list.sort()

for h in height_list:
    print(h)