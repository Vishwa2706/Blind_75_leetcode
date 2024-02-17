class Solution(object):
    def maxSubArray(self, nums):
        # Initialize variables to keep track of maximum sum so far and current sum
        max_sum = nums[0]  # Initialize with the first element of the array
        current_sum = nums[0]

        # Iterate through the array starting from the second element
        for num in nums[1:]:
            # The current sum can either continue with the current element or start anew
            current_sum = max(num, current_sum + num)
            # Update the maximum sum seen so far
            max_sum = max(max_sum, current_sum)

        return max_sum

# Example usage:
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
solution = Solution()
print(solution.maxSubArray(nums))  # Output should be 6, which is the sum of [4, -1, 2, 1]
