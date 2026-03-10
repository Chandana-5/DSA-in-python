#selection sort
#algorith:
#1.traverse the array from index 0 to N-1
#2.comapare current element with remaining elements
#3.swap if smaller element is found
#4.continue untill array becomes sorted 
#time complexity:o(N^2)
#space complexity:o(1)
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



