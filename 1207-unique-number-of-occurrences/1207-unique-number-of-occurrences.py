class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occ_list = []
        
        for i in set(arr):
            occ_list.append(arr.count(i))
            
        return len(set(occ_list)) == len(set(arr))