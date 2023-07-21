import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**8)
N, M = map(int, input().split())

parents = list(range(N+1))

def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]

edges = []
for _ in range(M):
    u, v = map(int, input().split())
    edges.append((u,v))

edges.sort()

for u, v in edges:    
    u_par = find(u)
    v_par = find(v)

    if u_par != v_par:
        if u_par < v_par:
            parents[u_par] = v_par
        else:
            parents[v_par] = u_par
ans = set()
for i in range(1,N+1):
    ans.add(find(i))

print(len(ans))