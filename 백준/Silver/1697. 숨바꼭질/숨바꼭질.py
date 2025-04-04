from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dp = [-1] * 100001
queue = deque()
queue.append(n)
dp[n] = 0

while queue:
    current = queue.popleft()

    if current == k:
        break

    for next_pos in [current - 1, current + 1, current * 2]:
        if 0 <= next_pos <= 100000 and dp[next_pos] == -1:
            dp[next_pos] = dp[current] + 1
            queue.append(next_pos)

print(dp[k])