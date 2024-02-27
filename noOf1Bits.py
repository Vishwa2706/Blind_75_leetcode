class Solution(object):
    def hammingWeight(self, n):
        count = 0
        # Loop until n becomes 0
        while n != 0:
            # Increment count if the least significant bit is set (i.e., if n is odd)
            count += n & 1
            # Right shift n by 1 bit to check the next bit
            n >>= 1
        return count

       
        