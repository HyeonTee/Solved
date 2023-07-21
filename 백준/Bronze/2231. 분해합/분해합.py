def assemble(n):
    n_str = str(n)
    result = n
    for i in n_str:
        result += int(i)
    return result

N = int(input())
ans = 0
for i in range(1,N):
    if assemble(i) == N:
        ans = i
        break

print(ans)