val = {"black":0,
	   "brown":1,
	   "red":2,
	   "orange":3,
	   "yellow":4,
	   "green":5,
	   "blue":6,
	   "violet":7,
	   "grey":8,
	   "white":9}

value = (val[input()] * 10 + val[input()]) * (10 ** val[input()])

print(value)