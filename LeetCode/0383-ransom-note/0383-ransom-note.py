class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r_dict = {}
        m_dict = {}
        
        for r in ransomNote:
            r_dict[r] = r_dict.get(r, 0) + 1
        
        for m in magazine:
            m_dict[m] = m_dict.get(m, 0) + 1
        
        for key, value in r_dict.items():
            if key not in m_dict or m_dict[key] < value:
                return False
        
        return True