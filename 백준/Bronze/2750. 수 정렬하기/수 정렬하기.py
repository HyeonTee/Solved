n = int(input())

ans_list = []
for _ in range(n):
    ans_list.append(int(input()))
    
ans_list = sorted(ans_list)

for ans in ans_list:
    print(ans)