# union-find 자료구조, union 시 더 작은 값이 대표값이 되도록 했음
def find(x):
    if parents[x] == x:
        return x
    else:
        return find(parents[x])
def union(a, b):
    global parents
    a = find(a)
    b = find(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

def solution(n, computers):
    answer = []
    
    global parents
    parents = list(range(n))
    
    for i in range(n):
        for j in range(n):
            if computers[i][j]:
                union(i,j)
    for i in range(n):
        answer.append(find(i))
    answer = set(answer)
    
    return len(answer)