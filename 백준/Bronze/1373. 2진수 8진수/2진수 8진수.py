import sys
input = sys.stdin.readline

binary = input().rstrip()
n = len(binary)

decimal = int(binary, 2)

print(format(decimal, 'o'))