#algorithm
#1.start with first element of the array
#2.compare the current element with the next element 
#3.if current element is grater than next,swap them
#4.move to the next pair and repeat the comparision
#5.continue untill the end of array
#6.after each pass,the largest element is placed at correct position
#7.repeat process for remaining unsorted part of array
#8.stop when no swaps are needed or after n-1 passes 
#time complexit O(n^2)
#space complexity O(1)
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


