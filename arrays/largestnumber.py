#Brutte force
#algorithm 
#1.sort array in ascending order
#2.print(size of array -1)th element
#Time complexity O(N log N)
#space complexity O(1)
class solution:
    def largestelement(self,nums):
        nums.sort()
        return nums[-1


        
#optimal opproach
#algorithm
#1.create variable largest
#2.initialize with first element
#3.use loop for rest element
#4.compare current element with largest
#5.if greater than update largest 
#Time complexity O(N)
#space complexity O(1)
class Solution:
    def largestElement(self, nums):
        n=len(nums)
        largest=nums[0]
        for i in range(n):
            if nums[i]>largest:
                largest=nums[i]
        return largest
        

