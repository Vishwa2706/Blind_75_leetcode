class Solution(object):
    def maxProduct(self, nums):
        if not nums:
            return 0
        
        # Initialize variables to store the maximum and minimum product ending at the current index
        max_product = nums[0]
        min_product = nums[0]
        
        # Initialize the overall maximum product
        max_overall = nums[0]
        
        # Loop through the array starting from the second element
        for num in nums[1:]:
            # If the current number is negative, swap the maximum and minimum product
            # Because multiplying a negative number with a minimum product can result in a maximum product
            if num < 0:
                max_product, min_product = min_product, max_product
            
            # Update the maximum and minimum product ending at the current index
            max_product = max(num, max_product * num)
            min_product = min(num, min_product * num)
            
            # Update the overall maximum product if necessary
            max_overall = max(max_overall, max_product)
        
        return max_overall

    
# Example usage:
nums = [2, 3, -2, 4]
solution = Solution()
print(solution.maxProduct(nums))  # Output: 6 (from the subarray [2, 3])
