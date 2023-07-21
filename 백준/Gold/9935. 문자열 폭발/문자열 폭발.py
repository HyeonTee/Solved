word = list(input())
bomb = input()
bomb_len = len(bomb)

stack = []

for w in word:
    stack.append(w)
    if ''.join(stack[-bomb_len:]) == bomb:
        del stack[-bomb_len:]

result = ''.join(stack)
if result:
    print(result)
else:
    print("FRULA")