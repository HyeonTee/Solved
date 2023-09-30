n, b = input().split()

dict = {}
for i in range(10):
	dict[str(i)] = i
for i in range(10, 36):
	dict[chr(i+55)] = i

n_list = list(n)
n_len = len(n)
b = int(b)

ans = 0
for i in range(n_len):
	tmp = dict[n_list[i]] * (b ** (n_len - i - 1))
	ans += tmp

print(ans)