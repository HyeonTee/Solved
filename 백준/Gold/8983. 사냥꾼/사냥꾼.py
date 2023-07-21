import sys

M, N, L = map(int, sys.stdin.readline().split())

shot_points = list(map(int, sys.stdin.readline().split()))
shot_points.sort()

animals = []
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    animals.append((x, y))

cnt = 0

for x, y in animals:
    lt = 0
    rt = M-1

    while lt <= rt:
        mid = (lt + rt) // 2
        if shot_points[mid] < x:
            lt = mid + 1
        else:
            rt = mid - 1

    if lt >= M or abs(shot_points[lt] - x) + y > L:
        if abs(shot_points[lt-1] - x) + y <= L:
            cnt += 1
    else:
        cnt += 1

print(cnt)