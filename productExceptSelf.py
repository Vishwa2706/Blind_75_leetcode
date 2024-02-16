class Solution(object):
    def productExceptSelf(self,nums):
        n = len(nums)
        # Initialize arrays to store the prefix and suffix products
        left_product = [1] * n
        right_product = [1] * n

        # Calculate prefix products
        for i in range(1, n):
            left_product[i] = left_product[i - 1] * nums[i - 1]

        # Calculate suffix products
        for i in range(n - 2, -1, -1):
            right_product[i] = right_product[i + 1] * nums[i + 1]

        # Multiply prefix and suffix products to get the result
        result = [left_product[i] * right_product[i] for i in range(n)]

        return result