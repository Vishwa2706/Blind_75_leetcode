class Solution(object):
    def maxArea(self, height):
        max_area = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            # Calculate the area between the two lines
            area = min(height[left], height[right]) * (right - left)
            # Update max_area if the current area is greater
            max_area = max(max_area, area)
            
            # Move the pointer pointing to the smaller line inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area

# Example usage:
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
solution = Solution()
print(solution.maxArea(height))  # Output should be 49

        
        