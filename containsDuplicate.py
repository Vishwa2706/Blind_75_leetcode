class Solution(object):
    def containsDuplicate(self, nums):
        # Create an empty set to store unique elements
        seen = set()
        
        # Iterate through the array
        for num in nums:
            # If the element is already in the set, return True
            if num in seen:
                return True
            # Otherwise, add the element to the set
            seen.add(num)
        
        # If no duplicates are found, return False
        return False

# Example usage:
nums1 = [1, 2, 3, 4, 5]
nums2 = [1, 2, 3, 4, 1]

sol = Solution()
print(sol.containsDuplicate(nums1))  # Output: False
print(sol.containsDuplicate(nums2))  # Output: True