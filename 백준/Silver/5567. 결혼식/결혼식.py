import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

edges = {}
invited = [0] * (n+1)

for i in range(1,n+1):
    edges[i] = []

for _ in range(m):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

for e1 in edges[1]:
    invited[e1] = 1
    for e2 in edges[e1]:
        invited[e2] = 1

if sum(invited):
    print(sum(invited)-1)
else:
    print(0)