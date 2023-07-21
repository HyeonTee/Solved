n, k = map(int, input().split())

if k < 5:
    print(0)
    exit()
elif k == 26:
    print(n)
    exit()

ans = 0
learned_bit = 0

for c in ['a','n','t','i','c']:
    learned_bit |= 1 << (ord(c)-ord('a'))

word_bits = []
for _ in range(n):
    word_bit = 0
    word = input()
    for w in word:
        word_bit |= (1 << (ord(w)-ord('a')))
    word_bits.append(word_bit)

def recur(idx, cnt):
    global ans
    global learned_bit
    if cnt == k - 5:
        read = 0
        for word_bit in word_bits:
            if (learned_bit & word_bit) == word_bit:
                read += 1
            
        ans = max(ans, read)
        return
    
    for i in range(idx, 26):
        if not learned_bit & (1 << i):
            learned_bit |= (1 << i)
            recur(i, cnt + 1)
            learned_bit ^= (1 << i)
    
recur(0,0)

print(ans)