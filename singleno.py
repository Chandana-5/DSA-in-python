class Solution:
    def singleNumber(self, nums):
        xorr=0
        for elements in nums:
            xorr^=elements
        return xorr
        