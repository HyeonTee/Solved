from collections import deque

def can_change(str1, str2):
    cnt = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            cnt += 1
    return cnt == 1

def solution(begin, target, words):
    if target not in words:
        answer = 0
    else:
        edges = {}
        edges[begin] = []
        visited = {}
        dist = {}
        dist[begin] = 0
        for w in words:
            edges[w] = []
            dist[w] = 0
            visited[w] = False
            if can_change(begin,w):
                edges[begin].append(w)
                
        for w1 in words:
            for w2 in words:
                #visited[w1][w2] = False
                #visited[w2][w1] = False
                if can_change(w1,w2):
                    edges[w1].append(w2)
                    edges[w2].append(w1)
        q = deque()
        q.append(begin)
        while q:
            v = q.popleft()
            for w in edges[v]:
                if not visited[w]:
                    visited[w] = True
                    dist[w] = dist[v] + 1
                    q.append(w)
        answer = dist[target]

    return answer