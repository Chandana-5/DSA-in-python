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
