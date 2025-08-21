from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        R_idx = deque()
        D_idx = deque()
        for i in range(n):
            if senate[i] == "R":
                R_idx.append(i)
            else:
                D_idx.append(i)
        
        while R_idx and D_idx:
            r = R_idx.popleft()
            d = D_idx.popleft()
            
            if r > d:
                D_idx.append(d + n)
            else:
                R_idx.append(r + n)
        
        if R_idx:
            return "Radiant"
        else:
            return "Dire"
                
        