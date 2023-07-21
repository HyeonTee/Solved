import sys
input = sys.stdin.readline

N = int(input())

conf_list = [0] * N
for i in range(N):
    s, f = map(int, input().split())
    conf_list[i] = (f, s)

conf_list.sort()

ans_list = [conf_list[0]]
k = 0
for i in range(1, len(conf_list)):
    if conf_list[i][1] >= conf_list[k][0]:
        ans_list.append(conf_list[i])
        k = i

print(len(ans_list))