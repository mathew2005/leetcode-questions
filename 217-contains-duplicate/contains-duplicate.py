class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # freqSet = set()

        # for num in nums:
        #     if num in freqSet:
        #         return True
        #     else:
        #         freqSet.add(num)
        # return False


        # sort the list and have 2 pointers
        nums.sort()
        prev = 0
        curr = 1
        while curr < len(nums):
            if nums[prev] == nums[curr]:
                return True
            prev += 1
            curr += 1

        return False