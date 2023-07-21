import sys
input = sys.stdin.readline

k, n = map(int, input().split())

wires = [0] * k
for i in range(k):
    wires[i] = int(input())

def cut(len):
    result = 0
    for wire in wires:
        result += wire//len
    return result

lt = 1
rt = max(wires)

while lt <= rt:
    mid = (lt+rt)//2
    if cut(mid) < n:
        rt = mid-1
    else:
        lt = mid+1

print(rt)