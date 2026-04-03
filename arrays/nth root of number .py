#brutte
#algorithm
#1.Start a loop from 1 to m for linear search.
#2.For each value in the loop, compute the value raised to power n.
#3.If the result equals m, return that value.
#4.If the result exceeds m, break the loop as the nth root does not exist as an integer.
#5.If no exact match is found, return -1 to indicate failure.
#time complexity O(M)
#space complexity O(1)
class Solution:
    def nthRoot(self, n, m):
        for i in range(1, m + 1):
            power = i ** n
            if power == m:
                return i
            if power > m:
                break
        return -1
#optimal 
#algorithm
#1.Start binary search with low as 1 and high as M.
#2.Find mid of the range and multiply it with itself N times to get Nth power of mid.If Nth power of mid equals M, return mid as the N-th root.
#3.If Nth power of mid is less than M, shift search to the right half.
#4.If Nth power of mid is greater than M, shift search to the left half.
#5.If no integer root is found after the loop, return -1.
#time complexity O(logM)
#space complexity O(1)
class Solution:
    def nthRoot(self, n, m):
        low, high = 1, m
        while low <= high:
            mid = (low + high) // 2
            ans = 1
            for _ in range(n):
                ans *= mid
                if ans > m:
                    break
            if ans == m:
                return mid
            if ans < m:
                low = mid + 1
            else:
                high = mid - 1
        return -1
