class Solution:
    def secondLargestElement(self, nums):
        n=len(nums)
        largest=nums[0]
        secondlargest=-1
        for i in range(0,n):
            if nums[i]>largest:
                largest=nums[i]
        for i in range(0,n):
            if nums[i]>secondlargest and nums[i]<largest:
                secondlargest=nums[i]
        return secondlargest

        
        