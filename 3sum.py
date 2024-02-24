class Solution:
    def threeSum(self, nums):
        nums.sort()
        ans = []
        for i, num in enumerate(nums):
            if i >= 1:
                if nums[i-1]==nums[i]:
                    continue
            l,r = i+1, len(nums)-1
            while l < r:
                total = num + nums[l]+nums[r]
                if total > 0:
                    r-=1
                elif total < 0:
                    l+=1
                else:
                    ans.append([num, nums[l], nums[r]])
                    l+=1
                    while l < r and nums[l-1]==nums[l]:
                        l+=1
        return ans

    
sol = Solution()
nums = [0,1,1]
print(sol.threeSum(nums))

# EXPLANATION
        
# Class Definition: The code defines a class named Solution.

# Function threeSum: This function takes a list of integers nums as input and returns a list of lists containing unique triplets that sum up to zero.

# Sorting the Input List: The nums list is sorted in non-decreasing order using the sort() method. Sorting the array is a crucial step in this algorithm.

# Iterating Through the Sorted List: The code iterates over each element num in the sorted list nums using enumerate() which also gives the index i.

# Duplicate Check: Within the loop, it checks if the current element is not the first element and if the previous element is the same as the current one. This check is done to avoid duplicate triplets. If duplicates are found, it skips to the next iteration using continue.

# Initializing Pointers: Two pointers l and r are initialized. l starts from i + 1 and r starts from the last element of the array.

# Two Pointer Technique: It uses a while loop with two pointers (l and r) to find triplets that sum up to zero.

# If the sum of current num, nums[l], and nums[r] is greater than 0, it decrements r to decrease the sum.
# If the sum is less than 0, it increments l to increase the sum.
# If the sum is exactly 0, it appends the triplet [num, nums[l], nums[r]] to the ans list.
# Handling Duplicates: While incrementing l after finding a triplet, it also checks for duplicates and skips over them.

# Returning the Answer: Finally, the function returns the list ans containing all unique triplets that sum up to zero.

# Testing: An instance of the Solution class is created, and the threeSum function is called with a sample input [0,1,1], and the result is printed. This will print all the unique triplets that sum up to zero in the input list.