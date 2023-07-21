import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))
oper_list = list(map(int, input().split()))

sum_num = oper_list[0]
sub_num = oper_list[1]
mul_num = oper_list[2]
div_num = oper_list[3]

max_result = -float('inf')
min_result = float('inf')

def dfs(idx, result, sum, sub, mul, div):
    global max_result, min_result

    if idx == N:
        max_result = max(max_result, result)
        min_result = min(min_result, result)
        return

    if sum:
        dfs(idx+1, result+num_list[idx], sum-1, sub, mul, div)
    if sub:
        dfs(idx+1, result-num_list[idx], sum, sub-1, mul, div)
    if mul:
        dfs(idx+1, result*num_list[idx], sum, sub, mul-1, div)
    if div:
        dfs(idx+1, int(result/num_list[idx]), sum, sub, mul, div-1)

dfs(1, num_list[0], sum_num, sub_num, mul_num, div_num)

print(max_result)
print(min_result)