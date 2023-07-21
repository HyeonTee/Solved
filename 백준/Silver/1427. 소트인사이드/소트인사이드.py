num_list = list(map(int, input()))

num_list.sort()

ans = ''
for num in num_list:
    ans = str(num) + ans

print(ans)