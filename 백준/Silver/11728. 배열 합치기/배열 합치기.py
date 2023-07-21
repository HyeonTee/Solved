import sys
input = sys.stdin.readline

n, m = map(int, input().split())

a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

a = 0
b = 0

while a < n and b < m:
    if a_list[a] < b_list[b]:
        print(a_list[a], end = " ")
        a += 1
    else:
        print(b_list[b], end = " ")
        b += 1

if a < n:
    print(*a_list[a:])

if b < m:
    print(*b_list[b:])