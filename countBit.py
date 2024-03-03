class Solution(object):
    def countBits(self, n):
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            # Count the number of set bits in i by adding the count of set bits in i // 2
            # and the least significant bit of i.
            ans[i] = ans[i >> 1] + (i & 1)
        return ans