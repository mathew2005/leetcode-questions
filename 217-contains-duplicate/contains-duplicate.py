class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # sort the list and have 2 pointers
        
        freqSet = set()

        for num in nums:
            if num in freqSet:
                return True
            else:
                freqSet.add(num)
        return False