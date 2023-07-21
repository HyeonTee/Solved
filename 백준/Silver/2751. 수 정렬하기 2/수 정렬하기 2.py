import sys

n = int(input())

num_list = []
for _ in range(n):
    num_list.append(int(sys.stdin.readline().strip()))

num_list = sorted(num_list)

for n in num_list:
    print(n)