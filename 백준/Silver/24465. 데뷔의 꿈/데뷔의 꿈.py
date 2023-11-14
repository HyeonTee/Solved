import sys
input = sys.stdin.readline

def zodiac(m, d):
	if (m == 1 and d >= 20) or (m == 2 and d <= 18):
		return 1
	if (m == 2 and d >= 19) or (m == 3 and d <= 20):
		return 2
	if (m == 3 and d >= 21) or (m == 4 and d <= 19):
		return 3
	if (m == 4 and d >= 20) or (m == 5 and d <= 20):
		return 4
	if (m == 5 and d >= 21) or (m == 6 and d <= 21):
		return 5
	if (m == 6 and d >= 22) or (m == 7 and d <= 22):
		return 6
	if (m == 7 and d >= 23) or (m == 8 and d <= 22):
		return 7
	if (m == 8 and d >= 23) or (m == 9 and d <= 22):
		return 8
	if (m == 9 and d >= 23) or (m == 10 and d <= 22):
		return 9
	if (m == 10 and d >= 23) or (m == 11 and d <= 22):
		return 10
	if (m == 11 and d >= 23) or (m == 12 and d <= 21):
		return 11
	if (m == 12 and d >= 22) or (m == 1 and d <= 19):
		return 12
	
members_zodiac = set()
for _ in range(7):
	month, day = map(int, input().split())
	members_zodiac.add(zodiac(month, day))

passed = []
n = int(input())
for _ in range(n):
	month, day = map(int, input().split())
	if zodiac(month, day) not in members_zodiac:
		passed.append((month, day))

if passed:
	passed.sort()
	for m, d in passed:
		print(m, d)
else:
	print("ALL FAILED")