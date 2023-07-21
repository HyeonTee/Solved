n = input()
word = list(input())

number = ['0','1','2','3','4','5','6','7','8','9']

hidden = ''
hidden_sum = 0
for w in word:
    if w in number:
        hidden = hidden + w
    else:
        if hidden != '':
            hidden_sum += int(hidden)
            hidden = ''

if hidden != '':
    hidden_sum += int(hidden)
print(hidden_sum)