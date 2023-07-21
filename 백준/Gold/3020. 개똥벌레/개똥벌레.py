import sys
input = sys.stdin.readline

n, h = map(int, input().split())

tops = [0] * (h+1)
bottoms = [0] * (h+1)

# O(n)
for i in range(n): # array[i]: 높이 i인 석순, 종유석의 갯수
    if i%2 == 0:
        bottoms[int(input())] += 1
    else:
        tops[int(input())] += 1

# O(n)
for i in range(1, h): # 누적합
    tops[h-i] += tops[h-i+1]
    bottoms[h-i] += bottoms[h-i+1]

min_break = n
min_count = 0

for i in range(1, h+1):
    if min_break > (bottoms[i] + tops[h-i + 1]):
        min_break = (bottoms[i] + tops[h-i + 1])
        min_count = 1
    elif min_break == (bottoms[i] + tops[h-i + 1]):
        min_count += 1

print(min_break, min_count)