import sys
from collections import Counter

N = int(sys.stdin.readline())

num_list = [0] * N
num_sum = 0

for i in range(N):
    num = int(sys.stdin.readline())
    num_list[i] = num
    num_sum += num

num_list.sort()

cnt = Counter(num_list)
cnt_most = cnt.most_common()
if len(cnt_most) > 1 and cnt_most[0][1] == cnt_most[1][1]:
    mode = cnt_most[1][0]
else:
    mode = cnt_most[0][0]

print(round(num_sum/N))
print(num_list[N//2])
print(mode)
print(num_list[-1] - num_list[0])