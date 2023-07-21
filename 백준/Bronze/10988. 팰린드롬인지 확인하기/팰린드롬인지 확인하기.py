word = input()

result = 1
for i in range(len(word)//2):
    if word[i] != word[-(i+1)]:
        result = 0
        
print(result)