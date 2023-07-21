N, M = map(int, input().split())

A = []
B = []

for _ in range(N):
    A.append(list(map(int, list(input()))))
for _ in range(N):
    B.append(list(map(int, list(input()))))

def turn(i,j):
    for x in range(i,i+3):
        for y in range(j,j+3):
            A[x][y] = 1 - A[x][y]

cnt = 0
if (N < 3 or M < 3) and A != B:
    cnt = -1
else:
    for row in range(N-2):
        for column in range(M-2):
            if A[row][column] != B[row][column]:
                cnt += 1
                turn(row, column)

if cnt != -1 and A != B:
    cnt = -1

print(cnt)