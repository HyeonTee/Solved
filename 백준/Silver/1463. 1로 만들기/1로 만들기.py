N = int(input())

dp_table = [0] * (N+1)

for i in range(2,N+1):
    dp_table[i] = dp_table[i-1] + 1

    if i%3 == 0:
        dp_table[i] = min(dp_table[i//3] + 1, dp_table[i])

    if i%2 == 0:
        dp_table[i] = min(dp_table[i//2] + 1, dp_table[i])

print(dp_table[N])