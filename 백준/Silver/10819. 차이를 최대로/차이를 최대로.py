import sys
from itertools import permutations

n = int(sys.stdin.readline().strip())

num_list = list(map(int, input().split()))

perms = list(permutations(num_list,n))

max_sub = 0
for perm in perms:
    sub = 0
    for i in range(0,len(perm)-1):
        sub += abs(perm[i]-perm[i+1])
    if sub > max_sub:
        max_sub = sub

print(max_sub)