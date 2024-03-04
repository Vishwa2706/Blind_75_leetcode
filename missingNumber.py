class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        expected_sum = n * (n + 1) // 2  # Sum of first n natural numbers

        actual_sum = sum(nums)  # Sum of numbers in the array

        return expected_sum - actual_sum

# Example usage:
nums = [3, 0, 1]  # Array with missing number 2
solution = Solution()
print(solution.missingNumber(nums))  # Output: 2

        
        