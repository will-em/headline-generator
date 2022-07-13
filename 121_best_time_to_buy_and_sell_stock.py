class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        left_ptr = 0 # Buy
        right_ptr = 1 # Sell

        max_profit = 0

        while right_ptr < len(prices):
            if prices[left_ptr] < prices[right_ptr]: # Profit
                max_profit = max(max_profit, prices[right_ptr] - prices[left_ptr])
            else: # Loss
                left_ptr = right_ptr

            right_ptr += 1

        return max_profit
