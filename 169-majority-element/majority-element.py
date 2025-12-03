class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # [2,2,3,3,3,3]
        # [1,1,1,1,2,3,]
        freqMap = {}
        currFreq = 0
        for num in nums:
            if num in freqMap:
                freqMap[num] +=1
            else:
                freqMap[num] = 1
        
        for num in nums:
            currFreq = freqMap[num]
            if currFreq > len(nums)/2:
                return num