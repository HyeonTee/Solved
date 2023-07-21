N = int(input())
num_list = list(map(int, input().split()))

temp = [1] * N
for j in range(N):
    for i in range(j):
        if num_list[i] < num_list[j]:
            temp[j] = max(temp[j], temp[i] + 1)

print(max(temp))