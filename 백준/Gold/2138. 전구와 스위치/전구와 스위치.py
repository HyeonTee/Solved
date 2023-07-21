import sys
input = sys.stdin.readline
INF = sys.maxsize

N = int(input())

A = list(map(int, input().rstrip()))
B = list(map(int, input().rstrip()))
cnt = 0

def toggle(bulb_list, *bulbs):
    for bulb in bulbs:
        bulb_list[bulb] = 1 - bulb_list[bulb]

A_temp = A[:]
toggle(A_temp, 0, 1)

def switch(K):
    cnt = 0
    for i in range(1,N):
        if K[i-1] == B[i-1]:
            continue
        cnt += 1
        if i < N-1:
            toggle(K, i-1,i,i+1)
        else:
            toggle(K, i-1, i)
    if K == B:
        return cnt
    else:
        return INF

ans = min(switch(A), switch(A_temp)+1)

if ans == INF:
    print(-1)
else:
    print(ans)