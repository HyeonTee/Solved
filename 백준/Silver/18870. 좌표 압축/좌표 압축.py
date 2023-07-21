import sys

N = int(sys.stdin.readline())

x_list = list(map(int, sys.stdin.readline().split()))

x_dict = {}
tag = 0

x_sorted = sorted(x_list)
x_dict[x_sorted[0]] = 0

for i in range(len(x_sorted) - 1):
    if x_sorted[i] < x_sorted[i+1]:
        tag += 1
        x_dict[x_sorted[i+1]] = tag

for x in x_list:
    print(x_dict[x], end = " ")