import sys
input = sys.stdin.readline

n = input()
nums = list(set(map(int, input().split())))
nums.sort()

print(*nums)