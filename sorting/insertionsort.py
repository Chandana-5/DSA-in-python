#algorithm
#1.start from the second element of array
#2.compare it with previous elements
#3.move all elements that are greater than current element one position ahead
#4.insert the current element in its correct position
#5.repeat untill the array is sorted
#time complexity O(n^2)
#space complexity O(1)
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


