#brutte force
#algorithm
#1.declare a set and insert all the elements of array into set
#2.number of unique elements i array is equal to size of the set
#3.traverse the set and fill the first k indices with elements in set
#time complexity - O(N)
#space complexity - O(N)
class Solution:
    def removeDuplicates(self,nums):
        seen=set()
        index=0
        for num in nums:
            if num not in seen:
                seen.add(num)
                nums[index]=num
                index+=1
        return index
#optimal solution
#algorithm
#1.check for unique element,run loop from 1 to n
#2.in case of unique element store in new array ,nums[k] 
#time complexity- O(N)
#space complexity - O(1)
    class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n=len(nums)
        k=1
        for i in range(1,n):
            if nums[i]!=nums[i-1]:
                nums[k]=nums[i]
                k+=1
        return k
