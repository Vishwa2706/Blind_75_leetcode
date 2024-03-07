class Solution(object):
    def coinChange(self,coins, amount):
        # Initialize an array to store the minimum number of coins needed for each amount
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0  # Base case: 0 coins needed for amount 0

        # Iterate through each coin denomination
        for coin in coins:
            # Update dp[i] if using this coin reduces the number of coins needed
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)

        # If dp[amount] is still float('inf'), it means amount cannot be made up
        if dp[amount] == float('inf'):
            return -1
        else:
            return dp[amount]


        