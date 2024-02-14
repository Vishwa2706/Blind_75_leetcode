class Solution(object):
    def twoSum(self, nums, target):
        # Create a dictionary to store the index of each number
        num_indices = {}
        
        # Iterate through the array
        for i, num in enumerate(nums):
            # Calculate the complement of the current number needed to reach the target
            complement = target - num
            # Check if the complement exists in the dictionary
            if complement in num_indices:
                # If it does, return the indices of the current number and its complement
                return [num_indices[complement], i]
            # Otherwise, store the index of the current number in the dictionary
            num_indices[num] = i

# Example usage:
nums = [2, 7, 11, 15]
target = 9
solution = Solution()
print(solution.twoSum(nums, target))  # Output: [0, 1] (since nums[0] + nums[1] = 2 + 7 = 9)
