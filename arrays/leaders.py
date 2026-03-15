class solution:
  def leaders(self,nums):
    n=len(nums)
    ans=[]
    max_val=nums[-1]
    ans.append(max_val[-1])
    for i in range(n-2,-1,-1):
      if nums[i]>max_val:
        ans.append(nums[i])
        max_val=nums[i]
    ans.reverse()
    return ans
