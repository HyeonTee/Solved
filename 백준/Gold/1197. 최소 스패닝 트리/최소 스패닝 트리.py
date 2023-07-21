import sys

input = sys.stdin.readline

V, E = map(int, input().split())

edges = []
visited = set()
ans = 0
parents = list(range(V+1))

def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]
    
for _ in range(E):
    a, b, c = map(int, input().split())
    edges.append((c,a,b))

edges.sort()

for cost,u,v in edges:
    u_par = find(u)
    v_par = find(v)
    if u_par != v_par:
        if u_par < v_par:
            parents[u_par] = v_par
        else:
            parents[v_par] = u_par

        ans += cost

print(ans)