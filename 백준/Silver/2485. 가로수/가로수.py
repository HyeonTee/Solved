import sys
input = sys.stdin.readline

def getGCD(a, b):
	if (b == 0):
		return a
	else:
		return getGCD(b, a % b)

n = int(input())
prev = int(input())

gaps = []
for i in range(n-1):
	curr = int(input())
	gaps.append(curr - prev)
	prev = curr

gcd = gaps[0]
for i in range(1, n-1):
	gcd = getGCD(gcd, gaps[i])

result = 0
for gap in gaps:
	result += (gap // gcd) - 1

print(result)