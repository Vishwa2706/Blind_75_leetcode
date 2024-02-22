class Solution(object):
    def search(self, nums, target):
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            # If we found the target, return its index
            if nums[mid] == target:
                return mid
            
            # Check if the left half is sorted
            if nums[left] <= nums[mid]:
                # Check if the target lies in the left half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # If the left half is not sorted, the right half must be sorted
            else:
                # Check if the target lies in the right half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        # If the target is not found, return -1
        return -1

# Example usage:
nums = [4,5,6,7,0,1,2]
target = 0
solution = Solution()
print(solution.search(nums, target))  # Output: 4 (index of the target)
