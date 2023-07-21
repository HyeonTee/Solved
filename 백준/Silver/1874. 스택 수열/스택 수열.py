import sys
input = sys.stdin.readline

n = int(input())

stack = []
result = []
num_idx = 1
ok = 1
for i in range(n):
    num = int(input())
    while num_idx <= num:
        stack.append(num_idx)
        num_idx += 1
        result.append('+')
    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        ok = 0

if ok == 0:
    print('NO')
else:
    for r in result:
        print(r)