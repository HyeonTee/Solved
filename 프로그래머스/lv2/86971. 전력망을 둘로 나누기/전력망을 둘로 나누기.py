def dfs(v, visited, edges):
    visited[v] = 1
    for w in edges[v]:
        if visited[w] == 0:
            dfs(w, visited, edges)

def solution(n, wires):
    answer = 100
    
    # 와이어 하나씩 없는 경우로 n번 dfs
    for i in range(n):
        edges = [[] for _ in range(n+1)]
        visited = [0] * (n+1)
        # wires에서 1~n번째 와이어까지 하나씩만 따로 continue 해서 빼줌
        for j, (v, w) in enumerate(wires):
            if i == j:
                continue
            edges[v].append(w)
            edges[w].append(v)
        # 1번 송전탑에서 dfs해주면 둘중 하나의 전력망(visited) 나옴
        dfs(1, visited, edges)
        # n-sum(visited)와 sum(visited) 두 전력망이 나오니 둘의 차중 최소값 return
        answer = min(abs(n-sum(visited)*2), answer)
        
    return answer