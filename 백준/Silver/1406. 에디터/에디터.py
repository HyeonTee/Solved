import sys
input = sys.stdin.readline

lt = list(input().strip())
rt = []
m = int(input())

for _ in range(m):
    command = input()

    if command[0] == 'L':
        if lt:
            rt.append(lt.pop())

    if command[0] == 'D':
        if rt:
            lt.append(rt.pop())

    if command[0] == 'B':
        if lt:
            lt.pop()

    if command[0] == 'P':
        lt.append(command[2])

rt = rt[::-1]
ans = lt + rt

for a in ans:
    print(a, end = "")