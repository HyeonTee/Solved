import sys
import heapq

N = int(input())
cards = []
plus = 0

for _ in range(N):
    heapq.heappush(cards, int(sys.stdin.readline()))

ans = 0

if N != 1:
    for i in range(N-1):
        deck_prev = heapq.heappop(cards)
        deck_cur = heapq.heappop(cards)

        new_deck = deck_prev + deck_cur
        ans += new_deck

        heapq.heappush(cards, new_deck)

print(ans)