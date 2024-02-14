class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0
        
        # Initialize variables
        min_price = prices[0]
        max_profit = 0
        
        # Iterate through the prices
        for price in prices:
            # Update the minimum price seen so far
            min_price = min(min_price, price)
            # Calculate the potential profit by selling at the current price
            # and buying at the minimum price seen so far
            max_profit = max(max_profit, price - min_price)
        
        return max_profit

# Example usage:
sol = Solution()
prices = [7, 1, 5, 3, 6, 4]
print(sol.maxProfit(prices))  # Output should be 5
