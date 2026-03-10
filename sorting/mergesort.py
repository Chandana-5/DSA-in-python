class Solution:
    def mergeSort(self, nums):
        self.divide(nums,0,len(nums)-1)
        return nums 
    def divide(self,nums,low,high):
        if low<high:
            mid=(low+high)//2 
            self.divide(nums,low,mid)
            self.divide(nums,mid+1,high)
            self.merge(nums,low,mid,high)
    def merge(self,nums,low,mid,high):
        left=low
        right=mid+1
        temp=[]
        while left<=mid and right<=high:
            if nums[left]<=nums[right]:
                temp.append(nums[left])
                left=left+1 
            else:
                temp.append(nums[right])
                right+=1 
        while left<=mid:
            temp.append(nums[left])
            left+=1 
        while right<=high:
            temp.append(nums[right])
            right+=1 
        for i in range(low,high+1):
            nums[i]=temp[i-low]
    
            
