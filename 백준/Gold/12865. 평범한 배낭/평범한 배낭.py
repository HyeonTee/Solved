import sys
input = sys.stdin.readline

N, K = map(int, input().split())

dp_table = [0] * (K+1)
items = []

for _ in range(N):
    w, v = map(int, input().split())
    items.append((w,v))

for w, v in items:
    for i in range(K, w-1,-1):
        dp_table[i] = max(dp_table[i], dp_table[i-w]+v)
        
print(max(dp_table))