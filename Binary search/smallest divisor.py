#brutte force
#algorithm
#1.We will run a loop from 1 to max element of the array to check all possible divisors.
#2.To calculate the result, we will iterate over the given array using a loop. Within this loop, we will divide each element in the array by the current divisor, and sum up the obtained ceiling values.
#3.Inside the outer loop, If result <= threshold: We will return d as our answer.
#4.Finally, if we are outside the nested loops, we will return -1.
#Time Complexity: O(max(arr[])*N)
#space complexity :O(1)
import math

class Solution:
    def smallestDivisor(self, arr, limit):
        n = len(arr)
        max_val = max(arr)
        for d in range(1, max_val + 1):
            total = 0
            for num in arr:
                total += math.ceil(num / d)
            if total <= limit:
                return d

        return -1  
#optimal 
#1.First, check if the number of elements is already greater than the allowed limit. If so, no answer is possible, so return -1.
T#2.hen, identify the largest number in the list.
#3.Start with two markers , one at the smallest possible number (1), and another at the largest number in the list.
#4.Use a loop to narrow down the range. In each step, find the number that is in the middle of the current range.
#5.Check if using this middle number as a divisor results in a total that is within the allowed limit. This is done using a helper that adds up the rounded-up results of each division.
#6.If the result is within the allowed limit, it means this number might work, but a smaller one could be better. So, look in the lower half of the current range.
#7.If the result is too large, it means this number is too small. So, look in the upper half of the range instead.
#8.Repeat this process until the range closes. The smallest number that works will be pointed to by the left marker, and that's the answer.
#time complexity O(log(max(arr[]))*N)
#space complexity O(1)
import math

class SmallestDivisorFinder:
    def sumByD(self, arr, div):
        return sum(math.ceil(x / div) for x in arr)
    def smallestDivisor(self, arr, limit):
        if len(arr) > limit:
            return -1

        low = 1
        high = max(arr)

        while low <= high:
            mid = (low + high) // 2
            if self.sumByD(arr, mid) <= limit:
                high = mid - 1 
            else:
                low = mid + 1   

        return low
