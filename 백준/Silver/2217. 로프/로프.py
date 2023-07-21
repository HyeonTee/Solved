import sys
input = sys.stdin.readline

N = int(input())

ropes = []
for _ in range(N):
    ropes.append(int(input()))

ropes.sort(reverse=True)

ans = 0
for i in range(N):
    ans = max(ans, ropes[i]*(i+1))

print(ans)