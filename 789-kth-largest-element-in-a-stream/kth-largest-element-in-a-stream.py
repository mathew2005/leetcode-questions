from heapq import heapify, heappop, heappush
class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        nums.sort(reverse=True)
        self.min_heap = nums[:]
        heapify(self.min_heap)
        while len(self.min_heap) > k:
            heappop(self.min_heap)

    def add(self, val: int) -> int:
        if len(self.min_heap) < self.k:
            heappush(self.min_heap, val)
        elif val > self.min_heap[0]:
            heappop(self.min_heap)
            heappush(self.min_heap,val)
        
        return self.min_heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)