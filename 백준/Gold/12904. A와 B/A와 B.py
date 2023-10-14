import sys
input = sys.stdin.readline

S = list(input().rstrip())
T = list(input().rstrip())

n = len(S)
turn = {"A": "B", "B": "A"}

while len(T) > n:
	if T[-1] == "A":
		T.pop()
	else:
		T.pop()
		T = T[::-1]
	
if S == T:
	print(1)
else:
	print(0)