class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_value = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):
            min_value = min(min_value, prices[i-1])
            
            max_profit = max(max_profit, prices[i] - min_value)

        return max_profit

#    max_clar = 0

#    # loop through prices
#    for i in range(1,len(prices)):
#       min_value = min(min_value, prices[i - 1])
#       curr_clar = prices[i] - min_value
#       max_clar = max(curr_clar, max_clar)
#    return max_clar