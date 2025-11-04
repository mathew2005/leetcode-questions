class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # same length
        # sort both s and t, check if s == t
        sMap = {}
        tMap = {}
        
        # loop through the string
        for char in s:
            if char not in sMap:
                sMap[char] = 1
            else:
                sMap[char] += 1

        for char in t:
            if char not in tMap:
                tMap[char] = 1
            else:
                tMap[char] += 1
                
        return sMap == tMap
            
        
        # T: O(nlogn + nlogn)
        # S:O(1)