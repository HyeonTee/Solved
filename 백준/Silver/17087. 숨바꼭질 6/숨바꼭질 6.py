import sys
input = sys.stdin.readline
from math import gcd
from functools import reduce

def multiple_gcd(numbers):
    return reduce(gcd, numbers)

n, s = map(int, input().split())
arr = list(map(int, input().split()))
for i in range(n):
    arr[i] = abs(s-arr[i])
    
print(multiple_gcd(arr))