#brutte force
#algorithm
#1.start from index i=0
#2.for every i compare it with all elements j=i+1 to n-1
#3.if nums[i]>nums[j]-return False
#4.if no such pair exists - return True
#time complexity O(N^2)
#space complexity O(N)

class solution:
    def issorted(self,nums):
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]>nums[j]:
                    return False
        return True
#optimal approach
#algorithm
#1.traverse array from 1 to n
#2.if nums[i] > nums[i+1]
#3.if loop finishes - return true
#time complexity O(N)
#space complexity O(1)
    class Solution:
    def check(self, nums):
        n=len(nums)
        for i in range(1,n):
            if nums[i]>=nums[i-1]:
                return True 
                i-=1
            else:
                return False
        
