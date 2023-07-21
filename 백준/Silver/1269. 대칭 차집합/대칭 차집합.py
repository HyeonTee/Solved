import sys
input = sys.stdin.readline

nA, nB = map(int, input().split())

A = set(map(int, input().split()))
B = set(map(int, input().split()))

nSum = len(A|B)

inter = nA + nB - nSum

print(nA + nB - inter*2)