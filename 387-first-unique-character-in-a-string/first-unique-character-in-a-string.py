class Solution:
    def firstUniqChar(self, s: str) -> int:
        freqMap = {}
        for string in s:
            if string in freqMap:
                freqMap[string] += 1
            else:
                freqMap[string] = 1
        
        indexMap = {}
        
        for i,string in enumerate(s):
            if string not in indexMap:
                indexMap[string] = i
        
    
        
        for key,val in freqMap.items():
            if val == 1:
                return indexMap[key] 
        return -1