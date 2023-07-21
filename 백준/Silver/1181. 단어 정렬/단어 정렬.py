import sys

N = int(input())

word_list = [None] * N
for i in range(N):
    word_list[i] = sys.stdin.readline().strip()

word_list = list(set(word_list))

word_list.sort()
word_list.sort(key = len)

for word in word_list:
    print(word)
