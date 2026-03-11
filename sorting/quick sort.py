#algorithm
#1.choose a pivot elements smaller than the pivot to left
#2.place all elements smaller than pivot to left
#3.place all elements grater than the pivot to right
#4.recursively apply the same process to the left and right subarrays
#5.continue untill the array becomes sorted 
#time complexity O(N log N)
#space complexity O(N)
class solution:
    def quicksort(self,nums):
        def partition(nums,low,high):
            pivot=nums[low]
            i=low
            j=high
            while i<j:
                while i<=high-1 and i<=pivot:
                    i=i+1
                while j>=low+1 and j>pivot:
                    j=j-1
                if i<j:
                     nums[i], nums[j] = nums[j], nums[i]
            nums[low],nums[j]=nums[j],nums[low]
            return j
        def qs(nums,low,high):
            while low<high:
                pIndex=partition(nums,low,high)
                qs(nums,low,pIndex-1)
                qs(nums,pIndex+1,high)
        qs(nums, 0, len(nums) - 1)
        return nums

