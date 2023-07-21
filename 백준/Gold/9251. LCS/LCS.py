X = input()
Y = input()

n = len(X)
m = len(Y)

X = '0' + X
Y = '0' + Y

dp_table = [[0] * (m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        if X[i] == Y[j]:
            dp_table[i][j] = dp_table[i-1][j-1] + 1
        else:
            dp_table[i][j] = max(dp_table[i][j-1], dp_table[i-1][j])

print(dp_table[n][m])