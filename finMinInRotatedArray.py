class Solution(object):
    def findMin(self, nums):
        # Edge case: if the array has only one element or is not rotated
        if len(nums) == 1 or nums[0] < nums[-1]:
            return nums[0]
        
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            # If the mid element is greater than the last element, minimum is on the right side
            if nums[mid] > nums[right]:
                left = mid + 1
            # If the mid element is less than the last element, minimum is on the left side including mid
            else:
                right = mid
                
        return nums[left]

# Example usage:
nums = [4,5,6,7,0,1,2]
solution = Solution()
print(solution.findMin(nums))  # Output: 0
