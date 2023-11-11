while True:
	try:
		S = input()

		lower = 0
		upper = 0
		num = 0
		space = 0
		for s in S:
			ord_s = ord(s)
			if 97 <= ord_s <= 122:
				lower += 1
			elif 65 <= ord_s <= 90:
				upper += 1
			elif ord_s == 32:
				space += 1
			else:
				num += 1
		
		print(lower, upper, num, space)
	except EOFError:
		break