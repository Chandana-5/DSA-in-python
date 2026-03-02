class Solution:
    def selectionSort(self, nums):
        N=len(nums)
        for i in range(0,N-1):
            for j in range(i+1,N):
                if nums[i]>nums[j]:
                    temp=nums[i]
                    nums[i]=nums[j]
                    nums[j]=temp
        return nums


