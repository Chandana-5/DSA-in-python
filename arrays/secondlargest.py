#Brute Force
#algorithm
#1.sort array in ascending order
#2.second element from last index is second largest
#time complexity O(N log N)
#space complexity O(1)
class solution:
    def secondlargestelement(self,nums):
        nums.sort()
        return nums[-2]

#optimal approach
#algorithm
#take variables largest and second largest
#assign first element to largest
#take -1 as second largest
#if current element is larger than largest update values of second largest and largest
#else if current element is larger than second largest update values of second largest
#after sorting second largest wiil be stored in second largest
#time complexity  O(N)
#space complexity O(1)
    
    class Solution:
    def secondLargestElement(self, nums):
        n=len(nums)
        largest=nums[0]
        secondlargest=-1
        for i in range(0,n):
            if nums[i]>largest:
                largest=nums[i]
        for i in range(0,n):
            if nums[i]>secondlargest and nums[i]<largest:
                secondlargest=nums[i]
        return secondlargest

        
        

