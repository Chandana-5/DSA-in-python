class Solution:
    def insertionSort(self, nums):
        N=len(nums)
        for i in range(1,N):
            j=i 
            while(j>0 and nums[j-1]>nums[j]):
                temp=nums[j-1]
                nums[j-1]=nums[j]
                nums[j]=temp 
                j=j-1
        return nums