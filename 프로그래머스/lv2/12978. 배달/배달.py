import heapq

def solution(N, road, K):
    answer = 0
    edges = [[0] * (N+1) for _ in range(N+1)]
    dist = [float('inf')] * (N+1)
    dist[1] = 0
    queue = []
    
    for a, b, c in road:
        if edges[a][b]:
            edges[a][b] = min(edges[a][b], c)
        else:
            edges[a][b] = c
        if edges[b][a]:
            edges[b][a] = min(edges[b][a], c)
        else:
            edges[b][a] = c
    
    heapq.heappush(queue, (dist[1], 1))
    while queue:
        curr_dist, curr_dest = heapq.heappop(queue)
        
        if dist[curr_dest] < curr_dist:
            continue
        
        for new_dest, new_dist in enumerate(edges[curr_dest]):
            if new_dist:
                distance = curr_dist + new_dist
                if distance < dist[new_dest]:
                    dist[new_dest] = distance
                    heapq.heappush(queue, (distance, new_dest))

    for d in dist:
        if d <= K:
            answer += 1
                
    return answer