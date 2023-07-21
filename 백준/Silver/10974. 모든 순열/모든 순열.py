from itertools import permutations

n = int(input())

num_list = list(range(1,n+1))

for perms in permutations(num_list, n):
    print(*perms)