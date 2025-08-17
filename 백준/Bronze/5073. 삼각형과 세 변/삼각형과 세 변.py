import sys
input = sys.stdin.readline

while True:
	side_list = list(map(int, input().split()))
	side_list.sort()
	if side_list[0] == 0 and side_list[1] == 0 and side_list[2] == 0:
		break
	if side_list[0] + side_list[1] <= side_list[2]:
		print("Invalid")
	elif side_list[0] == side_list[1] == side_list[2]:
		print("Equilateral")
	elif side_list[0] == side_list[1] or side_list[1] == side_list[2]:
		print("Isosceles")
	else:
		print("Scalene")