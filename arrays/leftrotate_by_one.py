#brutte force
#algorithm
#1.create a temporary array to to store the shifted elements
#2.shift the element to left by one position
#3.the first element moves to last positim
#time complexity- O(N)
#space complexity -O(N)
    def solver(arr,n):
        temp=[0]*n
        for i in range(1,nl):
            temp[i-1]=arr[i]
            temp[n-1]=arr[0]
            for num in temp:
                print(num,end="")
                print()
#optimal solution
#1.dtore the first element of the array in variable temp
#2.shift all elements one position to left
#3.place the sorted elemts at last position
#time complexity - O(n)
#space complexity-O(1)
    
class Solution:
    def rotateArrayByOne(self, nums):
        n=len(nums)
        temp=nums[0]
        for i in range(1,n):
            nums[i-1]=nums[i]
        nums[n-1]=temp 
        return n-1  
        
        
        
        
