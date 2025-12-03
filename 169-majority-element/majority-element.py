class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # [2,2,3,3,3,3]
        # [1,1,1,1,2,3,]
        nums.sort()
        return nums[len(nums) // 2]