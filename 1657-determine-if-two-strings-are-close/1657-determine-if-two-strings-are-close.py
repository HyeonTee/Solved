from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2) or set(word1) != set(word2):
            return False
        
        # memo1 = {}
        # for w1 in word1:
        #     if w1 not in memo1:
        #         memo1[w1] = 1
        #     else:
        #         memo1[w1] += 1
        memo1 = Counter(word1)
                
        # memo2 = {}
        # for w2 in word2:
        #     if w2 not in memo2:
        #         memo2[w2] = 1
        #     else:
        #         memo2[w2] += 1
        memo2 = Counter(word2)
                
        return sorted(list(memo1.values())) == sorted(list(memo2.values()))