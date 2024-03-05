class Solution:
    def reverseBits(self, n):
        reversed_bits = 0
        for _ in range(32):
            reversed_bits <<= 1
            reversed_bits |= n & 1
            n >>= 1
        return reversed_bits

# Example usage
solution = Solution()
result = solution.reverseBits(43261596)
print(result)  # Output: 964176192
