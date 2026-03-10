class Solution:
    def bubbleSort(self, nums):
        N=len(nums)
        for i in range(N-1):
            for j in range(0,N-i-1):
                if nums[j]>nums[j+1]:
                    temp=nums[j]
                    nums[j]=nums[j+1]
                    nums[j+1]=temp
        return nums
