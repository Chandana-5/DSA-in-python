class Solution:
    def check(self, nums):
        n=len(nums)
        for i in range(1,n):
            if nums[i]>=nums[i-1]:
                return True 
                i-=1
            else:
                return False
        
