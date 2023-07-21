import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

K = int(input())

def dfs(v):
    mark[v] = "visited"
    for w in edges[v]:
        if mark[w] != "visited":
            incident[w] = 1 - incident[v]
            dfs(w)

def dfs_all(G):
    for node in G:
        if mark[node] != "visited":
            dfs(node)

for _ in range(K):
    V, E = map(int, input().split())
    mark = {}
    edges = {}
    incident = {}
    e_list = []
    v_list = set()

    for i in range(1,V+1):
        mark[i] = None
        edges[i] = []
        incident[i] = 0
        
    for _ in range(E):
        v, w = map(int, input().split())
        edges[v].append(w)
        edges[w].append(v)
        e_list.append((v,w))
        v_list.add(v)
        v_list.add(w)

    dfs_all(v_list)

    ans = "YES"
    for v, w in e_list:
        if incident[v] == incident[w]:
            ans = "NO"
    
    print(ans)