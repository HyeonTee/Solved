import sys
input = sys.stdin.readline
#           0  1  2
#           3  4  5
#           6  7  8
#  9 10 11 18 19 20 27 28 29 36 37 38
# 12 13 14 21 22 23 30 31 32 39 40 41
# 15 16 17 24 25 26 33 34 35 42 43 44
#          45 46 47
#          48 49 50
#          51 52 53

#       o o o
#       o o o
#       o o o
# g g g w w w b b b y y y        B
# g g g w w w b b b y y y      L U R D
# g g g w w w b b b y y y        F
#       r r r
#       r r r
#       r r r

color = {0: 'o', 1: 'g', 2: 'w', 3: 'b', 4: 'y', 5: 'r'}
# cube = [0] * 54
# for i in range(54):
# 	cube[i] = color[i // 9]

#     6  7  8
# 11 18 19 20 27
# 14 21 22 23 30
# 17 24 25 26 33
#    45 46 47
def up_rotate():
	# 면 회전
	tmp = [cube[18], cube[19]]
	cube[18], cube[19] = cube[24], cube[21]
	cube[24], cube[21] = cube[26], cube[25]
	cube[26], cube[25] = cube[20], cube[23]
	cube[20], cube[23] = tmp[0], tmp[1]
	# 면에 인접한 부분 회전
	tmp = [cube[6], cube[7], cube[8]]
	cube[6], cube[7], cube[8] = cube[17], cube[14], cube[11]
	cube[17], cube[14], cube[11] = cube[47], cube[46], cube[45]
	cube[47], cube[46], cube[45] = cube[27], cube[30], cube[33]
	cube[27], cube[30], cube[33] = tmp[0], tmp[1], tmp[2]

#     2  1  0
# 29 36 37 38  9
# 32 39 40 41 12
# 35 42 43 44 15
#    53 52 51
def down_rotate():
	# 면 회전
	tmp = [cube[36], cube[37]]
	cube[36], cube[37] = cube[42], cube[39]
	cube[42], cube[39] = cube[44], cube[43]
	cube[44], cube[43] = cube[38], cube[41]
	cube[38], cube[41] = tmp[0], tmp[1]
	# 면에 인접한 부분 회전
	tmp = [cube[2], cube[1], cube[0]]
	cube[2], cube[1], cube[0] = cube[35], cube[32], cube[29]
	cube[35], cube[32], cube[29] = cube[51], cube[52], cube[53]
	cube[51], cube[52], cube[53] = cube[9], cube[12], cube[15]
	cube[9], cube[12], cube[15] = tmp[0], tmp[1], tmp[2]

#    24 25 26
# 17 45 46 47 33
# 16 48 49 50 34
# 15 51 52 53 35
#    44 43 42
def front_rotate():
	# 면 회전
	tmp = [cube[45], cube[46]]
	cube[45], cube[46] = cube[51], cube[48]
	cube[51], cube[48] = cube[53], cube[52]
	cube[53], cube[52] = cube[47], cube[50]
	cube[47], cube[50] = tmp[0], tmp[1]
	# 면에 인접한 부분 회전
	tmp = [cube[24], cube[25], cube[26]]
	cube[24], cube[25], cube[26] = cube[15], cube[16], cube[17]
	cube[15], cube[16], cube[17] = cube[42], cube[43], cube[44]
	cube[42], cube[43], cube[44] = cube[33], cube[34], cube[35]
	cube[33], cube[34], cube[35] = tmp[0], tmp[1], tmp[2]

#     38 37 36
#  9   0  1  2 29
# 10   3  4  5 28
# 11   6  7  8 27
#     18 19 20
def back_rotate():
	# 면 회전
	tmp = [cube[0], cube[1]]
	cube[0], cube[1] = cube[6], cube[3]
	cube[6], cube[3] = cube[8], cube[7]
	cube[8], cube[7] = cube[2], cube[5]
	cube[2], cube[5] = tmp[0], tmp[1]
	# 면에 인접한 부분 회전
	tmp = [cube[38], cube[37], cube[36]]
	cube[38], cube[37], cube[36] = cube[11], cube[10], cube[9]
	cube[11], cube[10], cube[9] = cube[20], cube[19], cube[18]
	cube[20], cube[19], cube[18] = cube[29], cube[28], cube[27]
	cube[29], cube[28], cube[27] = tmp[0], tmp[1], tmp[2]

#      0  3  6
# 38   9 10 11 18
# 41  12 13 14 21
# 44  15 16 17 24
#     51 48 45
def left_rotate():
	# 면 회전
	tmp = [cube[9], cube[10]]
	cube[9], cube[10] = cube[15], cube[12]
	cube[15], cube[12] = cube[17], cube[16]
	cube[17], cube[16] = cube[11], cube[14]
	cube[11], cube[14] = tmp[0], tmp[1]
	# 면에 인접한 부분 회전
	tmp = [cube[0], cube[3], cube[6]]
	cube[0], cube[3], cube[6] = cube[44], cube[41], cube[38]
	cube[44], cube[41], cube[38] = cube[45], cube[48], cube[51]
	cube[45], cube[48], cube[51] = cube[18], cube[21], cube[24]
	cube[18], cube[21], cube[24] = tmp[0], tmp[1], tmp[2]

#     8  5  2
# 20 27 28 29 36
# 23 30 31 32 49
# 26 33 34 35 42
#    47 50 53
def right_rotate():
	# 면 회전
	tmp = [cube[27], cube[28]]
	cube[27], cube[28] = cube[33], cube[30]
	cube[33], cube[30] = cube[35], cube[34]
	cube[35], cube[34] = cube[29], cube[32]
	cube[29], cube[32] = tmp[0], tmp[1]
	# 면에 인접한 부분 회전
	tmp = [cube[8], cube[5], cube[2]]
	cube[8], cube[5], cube[2] = cube[26], cube[23], cube[20]
	cube[26], cube[23], cube[20] = cube[53], cube[50], cube[47]
	cube[53], cube[50], cube[47] = cube[36], cube[39], cube[42]
	cube[36], cube[39], cube[42] = tmp[0], tmp[1], tmp[2]

def rotate(command):
	if command == "U+":
		up_rotate()
	if command == "D+":
		down_rotate()
	if command == "F+":
		front_rotate()
	if command == "B+":
		back_rotate()
	if command == "L+":
		left_rotate()
	if command == "R+":
		right_rotate()
	if command == "U-":
		for _ in range(3):
			up_rotate()
	if command == "D-":
		for _ in range(3):
			down_rotate()
	if command == "F-":
		for _ in range(3):
			front_rotate()
	if command == "B-":
		for _ in range(3):
			back_rotate()
	if command == "L-":
		for _ in range(3):
			left_rotate()
	if command == "R-":
		for _ in range(3):
			right_rotate()

T = int(input())
for _ in range(T):
	cube = [0] * 54
	for i in range(54):
		cube[i] = color[i // 9]
	n = input()
	command_list = list(input().split())
	for command in command_list:
		rotate(command)
	print(cube[18] + cube[19] + cube[20])
	print(cube[21] + cube[22] + cube[23])
	print(cube[24] + cube[25] + cube[26])