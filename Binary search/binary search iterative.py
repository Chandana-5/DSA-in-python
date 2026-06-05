class solution:
    def binarysearch(self,nums):
        n=len(nums)
        low=0
        high=n-1
        while low<=high:
            mid=(low+high)//2 
            if mid==target:
                return mid 
            else if mid>target:
                low=mid+1 
            else:
                high=mid-1 
        return -1
