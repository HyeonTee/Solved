import sys

N = int(sys.stdin.readline().strip())
N_set = set(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline().strip())
M_list = list(map(int, sys.stdin.readline().split()))

for m in M_list:
    if m in N_set:
        print(1)
    else:
        print(0)