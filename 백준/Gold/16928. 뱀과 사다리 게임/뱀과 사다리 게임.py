n, m = map(int, input().split())

board = [999999] * 101
board[1] = 0

ladder = {}
for _ in range(n+m):
    a, b = map(int, input().split())
    ladder[a] = b
    
for i in range(1, 100):
    if i in ladder:
        continue
    for j in range(1, 7):
        if (i+j) > 100:
            continue
        board[i+j] = min(board[i+j], board[i] + 1)
        if (i+j) in ladder:
            board[ladder[i+j]] = min(board[i+j], board[ladder[i+j]])

for i in range(1, 100):
    if i in ladder:
        continue
    for j in range(1, 7):
        if (i+j) > 100:
            continue
        board[i+j] = min(board[i+j], board[i] + 1)
        if (i+j) in ladder:
            board[ladder[i+j]] = min(board[i+j], board[ladder[i+j]])
    
print(board[100])