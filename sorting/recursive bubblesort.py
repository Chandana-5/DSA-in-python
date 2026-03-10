class Solution:
    def bubbleSort(self, nums):
        n=len(nums)
        temp=[]
        if n==1:
            return nums
        for i in range(n):
            for j in range(n-i-1):
                if nums[j]>nums[j+1]:
                    temp=nums[j]
                    nums[j]=nums[j+1]
                    nums[j+1]=temp 
        return nums
