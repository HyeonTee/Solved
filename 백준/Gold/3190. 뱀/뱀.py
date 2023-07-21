N = int(input())
K = int(input())

time = 0
snake = []
d = 0 # 오른쪽 아래 왼쪽 위

row = 0
col = 0

apple = []
for _ in range(K):
    a, b = map(int, input().split())
    apple.append((a-1, b-1))

L = int(input())
drive = []
drive_idx = 0

for _ in range(L):
    X, C = input().split()
    X = int(X)
    drive.append((X, C))


while True:
    time += 1
    snake.append((row, col))
    if d == 0:
        col += 1
    elif d == 1:
        row += 1
    elif d == 2:
        col -= 1
    else:
        row -= 1

    if row < 0 or row >= N or col < 0 or col >= N or (row, col) in snake:
        break

    if (row, col) in apple:
        apple.remove((row, col))
    else:
        snake.pop(0)

    if drive_idx < L and drive[drive_idx][0] == time:
        if drive[drive_idx][1] == "D":
            d = (d + 1) % 4
        else:
            d = (d - 1) % 4
        drive_idx += 1

print(time)