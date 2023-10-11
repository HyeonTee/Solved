import sys
input = sys.stdin.readline

def count_one(n):
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count

n, k = map(int, input().split())


cnt = 0
while count_one(n) > k:
	n += 1
	cnt += 1

print(cnt)