import sys
input = sys.stdin.readline
INF = sys.maxsize

n, m = map(int, input().split())
start, end, delete, add = map(int, input().split())

start -= 1
end -= 1

ladder = [0] + [int(input()) - 1 for _ in range(m)]

d = [[INF] * n for _ in range(m+1)]

for i in range(n):
    if i == start:
        d[0][i] = 0
    else:
        d[0][i] = abs(start - i) * add

for i in range(1, m+1):
    for j in range(n):
        for k in range(n):
            if k == j and (ladder[i] == k or ladder[i] + 1 == k):
                d[i][j] = min(d[i][j], d[i-1][k] + delete)
            elif (k <= ladder[i] and ladder[i] <= j - 1) or (j <= ladder[i] and ladder[i] <= k - 1):
                d[i][j] = min(d[i][j], d[i-1][k] + (abs(k-j) - 1) * add)
            else:
                d[i][j] = min(d[i][j], d[i-1][k] + abs(k - j) * add)

print(d[m][end])