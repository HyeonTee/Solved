import sys
input = sys.stdin.readline

change = {}

for i in range(65, 91):
	if (i + 13) < 91:
		change[chr(i)] = chr(i+13)
	else:
		change[chr(i)] = chr(i-13)

for i in range(97, 123):
	if (i + 13) < 123:
		change[chr(i)] = chr(i+13)
	else:
		change[chr(i)] = chr(i-13)

sentence = input().rstrip()

result = ""
for s in sentence:
	if s in change:
		result += change[s]
	else:
		result += s

print(result)