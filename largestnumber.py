class Solution:
    def largestElement(self, nums):
        n=len(nums)
        largest=nums[0]
        for i in range(n):
            if nums[i]>largest:
                largest=nums[i]
        return largest
        