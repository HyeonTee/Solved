import sys
input = sys.stdin.readline

n = int(input())

retult = ''
def is_good(numstr):
	mid = len(numstr) // 2
	for i in range(1, mid+1):
		if numstr[-i:] == numstr[-2*i : -i]:
			return False
	return True

def dfs(curr, cnt):
	if cnt == n:
		print(curr)
		exit()
	for num in "123":
		temp = curr + num
		if is_good(temp):
			dfs(temp, cnt + 1)

dfs('', 0)