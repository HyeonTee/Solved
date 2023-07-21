from itertools import permutations
import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

card_list = []
for _ in range(n):
    card = input()
    card_list.append(card)

nums = set()
cards = permutations(card_list, k)
for c in cards:
    n = ''.join(c)
    nums.add(n)

print(len(nums))