import sys
from itertools import combinations

N, M = map(int, input().split())

num_list = list(map(int, input().split()))

combs = list(combinations(num_list, 3))

sum_max = 0

for comb in combs:
    sum_now = sum(comb)
    if sum_now <= M:
        if sum_now > sum_max:
            sum_max = sum_now

print(sum_max)