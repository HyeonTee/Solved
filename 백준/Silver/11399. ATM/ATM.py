import sys
input = sys.stdin.readline

N = int(input())

time_list = list(map(int, input().split()))

time_list.sort()

takes = 0
ans = 0
for time in time_list:
    takes += time
    ans += takes

print(ans)