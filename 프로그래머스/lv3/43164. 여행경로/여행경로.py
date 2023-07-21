# 위상정렬 신찬수 교수님 풀이법!
answer = []
edges = {}

# 출발지에서 알파벳 순서 앞서는 목적지부터 dfs, 갈 곳 없을때 backtrace 하면서 append
def recur(v):
    while edges[v]:
        recur(edges[v].pop())
    if not edges[v]:
        answer.append(v)
        return

def solution(tickets):
    # edge 생성
    for start, end in tickets:
        edges[start] = []
        edges[end] = []
    for start, end in tickets:
        edges[start].append(end)
    
    # edges의 도착지를 내림차순으로 정렬, pop()할 때 순서 앞부터 dfs하기 위함
    for start, _ in edges.items():
        edges[start].sort(reverse = True)
    
    recur("ICN")
    
    return answer[::-1] # backtrace 하면서 append 했으니 역순으로 리턴