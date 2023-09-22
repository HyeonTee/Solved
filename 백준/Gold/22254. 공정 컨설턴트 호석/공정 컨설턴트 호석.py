import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n, x = map(int, input().split())

products = list(map(int, input().split()))

lt = 1
rt = n

def process(N):
    lines = [0] * N
    for product in products:
        next_line = heappop(lines)
        next_line += product
        if next_line > x:
            return False
        else:
            heappush(lines, next_line)        
    
    return True

while lt <= rt:
    mid = (lt + rt) // 2
    if process(mid):
        rt = mid - 1
    else:
        lt = mid + 1
    
print(lt)