#algorithm
#1.if size of array n1,stop
#2.compare adjacent elements from index 0 to n-2
#3.if nums[i]>nums[i+1],swap them
#4. after one pass the largest elemet moves to the last position
#5.recursively call bubblesort for the first n-1 elements 
#6.repeat untill array is sorted
#time complexity O(N^2)
#space complexity O(N)
class Solution:
    def bubbleSort(self, nums):
        n=len(nums)
        temp=[]
        if n==1:
            return nums
        for i in range(n-1):
                if nums[i]>nums[i+1]:
                    temp=nums[i]
                    nums[i]=nums[i+1]
                    nums[i+1]=temp 
        return nums

