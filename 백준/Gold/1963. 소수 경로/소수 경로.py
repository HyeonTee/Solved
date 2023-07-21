from collections import deque
from itertools import combinations

T = int(input())

primes = []

def is_linked(str1, str2):
    n = 0
    for i in range(4):
        if str1[i] == str2[i]:
            n += 1
    if n == 3:
        return True
    return False

for i in range(1000, 10000):
    is_prime = True
    for j in range(2, int(i**0.5+1)):
        if i % j == 0:
            is_prime = False
    if is_prime:
        primes.append(str(i))

edge = {}
for prime in primes:
    edge[prime] = []

for p1, p2 in combinations(primes, 2):
    if is_linked(p1, p2):
        edge[p1].append(p2)
        edge[p2].append(p1)

for _ in range(T):
    a, b = input().split()
    
    visited = {}
    dist = {}
    for p in primes:
        visited[p] = False
        dist[p] = 0
    
    queue = deque()
    queue.append(a)
    visited[a] = True

    while queue:
        v = queue.popleft()
        for w in edge[v]:
            if visited[w] == False:
                visited[w] = True
                dist[w] = dist[v] + 1
                queue.append(w)
    
    if dist[b] == 0:
        if a != b:
            print("Impossible")
        else:
            print(0)
    else:
        print(dist[b])