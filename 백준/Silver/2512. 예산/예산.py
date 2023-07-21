import sys
input = sys.stdin.readline

N = int(input())
budget_list = list(map(int, input().split()))
budget_max = int(input())

def allot(budget):
    result = 0
    for b in budget_list:
        if b < budget:
            result += b
        else:
            result += budget
    return result

lt = 0
rt = max(budget_list)

while lt <= rt:
    mid = (lt+rt)//2
    if allot(mid) <= (budget_max):
        lt = mid+1
    else:
        rt = mid-1

print(rt)