class Solution(object):
    def getSum(self, a, b):
        # 32-bit mask to get the last 32 bits
        mask = 0xFFFFFFFF
        
        # Convert a and b to 32 bits
        while b:
            # Perform addition without carry
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
            
        # Handle overflow
        return a if a <= 0x7FFFFFFF else ~(a ^ mask)