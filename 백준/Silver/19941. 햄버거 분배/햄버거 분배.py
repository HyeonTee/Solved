import sys
input = sys.stdin.readline

n, k = map(int, input().split())
table = list(input().strip())

cnt = 0
for idx in range(n):
    if table[idx] == 'P':
        for i in range(max(idx-k, 0), min(idx+k+1, n)):
            if table[i] == 'H':
                table[i] = 0
                cnt += 1
                break

print(cnt)