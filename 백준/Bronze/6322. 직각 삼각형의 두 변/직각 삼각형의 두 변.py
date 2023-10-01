import sys
input = sys.stdin.readline

n = 1
while True:
	a, b, c = map(int, input().split())
	if (a == 0 and b == 0 and c == 0):
		break

	if a == -1:
		if b >= c:
			print("Triangle #" + str(n))
			print("Impossible.")
		else:
			print("Triangle #" + str(n))
			print("a = %0.3f"%((c**2 - b**2) ** 0.5))

	if b == -1:
		if a >= c:
			print("Triangle #" + str(n))
			print("Impossible.")
		else:
			print("Triangle #" + str(n))
			print("b = %0.3f"%((c**2 - a**2) ** 0.5))

	if c == -1:
		print("Triangle #" + str(n))
		print("c = %0.3f"%((a**2 + b**2) ** 0.5))
	
	print()
	
	n += 1