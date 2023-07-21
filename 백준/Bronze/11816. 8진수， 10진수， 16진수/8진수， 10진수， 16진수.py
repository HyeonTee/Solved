n = input()

if n[0] == '0':
    if n[1] == 'x':
        num = int(n[2:], 16)
        print(num)
    else:
        num = int(n[1:], 8)
        print(num)
else:
    print(n)