class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = 0
        max_al = 0
        
        for g in gain:
            altitude += g
            max_al = max(altitude, max_al)
            
        return max_al