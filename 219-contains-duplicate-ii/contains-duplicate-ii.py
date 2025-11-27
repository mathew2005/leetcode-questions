class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # nums[i] == nums[j] && abs(i-j) <=k
        
        # intialize hashMap
        hashMap = {} # {number: index}

        # loop through nums
        for i in range(len(nums)):
            num = nums[i]

            # case 1: num exist in hashMap
            if num in hashMap and abs(i - hashMap[num]) <= k:
                return True
            # case 2: num doesn't exist in hashMap
            else:
                hashMap[num] = i
        return False

        #  nums = [1,2,3,1]
        # 1 -> {1:0}
        # 2 -> {1:0, 2:1,}
        # 3 -> {1:0, 2:1, 3:2}
        # 1 -> don't touch the hashmap and just do check abs(i-j) <=k