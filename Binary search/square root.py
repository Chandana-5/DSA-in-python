#optimal
#algorithm
#1.First, note that the answer lies between 1 and the given number n.
#2.Set the search range with the smallest value as 1 and the largest value as n.
#3.Use binary search within this range to test possible numbers.
#4.At each step, take the middle number and check if its square is less than or equal to n.
#5.If it is, record this number as a candidate and move right to check for a larger number.
#6.If the square is greater than n, move left to check smaller numbers.
#7.Continue this process until the range closes, and the largest recorded number will be the square root.
#time complexity O(log N)
#space complexity O(1)
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        left, right, ans = 1, x // 2, 0
        while left <= right:
            mid = (left + right) // 2
            if mid * mid <= x
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans
  #brutte
  #algorthim
  #1.Start by creating a variable called ans to hold the result and run a loop from 1 up to n.
#2.While the square of the current number is less than or equal to n, keep updating ans with that number.
#3.As soon as the square of the number becomes greater than n, stop the loop because no bigger number can be the answer.
#4.At the end, the value stored in ans will be the integer square root of n
#time complexity 0(N)
#space complexity 0(1)
def floorSqrt(self, n: int) -> int:
        ans = 0
        for i in range(1, n + 1):
            if i * i <= n:
                ans = i
            else:
                break
        return ans
