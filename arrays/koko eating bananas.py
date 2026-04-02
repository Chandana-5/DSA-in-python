#brutte
#algorithm
#1.Find the largest pile size (max of the array).
#2.Loop through all possible speeds from 1 to this maximum value.
#3.For each speed, calculate the total hours needed. For each pile, compute the time as ceil(pile / speed).
#4.Sum up the hours for all piles.
#5.If the total hours is less than or equal to the allowed hours, return this speed as the answer.
#time complexity O(n * max(a[]))
#Space Complexity: O(1)
import math

class Solution:
    def calculateTotalHours(self, a, hourly):
        totalHours = 0
        for pile in a:
            totalHours += math.ceil(pile / hourly)
        return totalHours
    def minEatingSpeed(self, a, h):
        maxVal = max(a)
        for i in range(1, maxVal + 1):
            hours = self.calculateTotalHours(a, i)
            if hours <= h:
                return i
        return maxVal
#optimal
#algorithm
#1.First, identify the largest pile size since the eating speed cannot be more than that.
#2.Set the search range with the lowest speed as 1 and the highest speed as the maximum pile size.
#3.Use binary search within this range to check possible speeds.
#4.At each step, take the middle value as the current speed and calculate how many hours it would take to finish all piles at this speed.
#5.If the total hours are less than or equal to the allowed hours, this speed is a candidate, so try to see if a smaller speed also works by moving left.
#6.If the total hours exceed the allowed hours, then the speed is too slow, so move right to try higher speeds.
#7.Continue this process until the range closes, and the smallest valid speed found will be the answer.
#time complexity O(N*log(max(a[])))
#space complexity O(1)
import math

class Solution:
    # Function to calculate total hours at given speed
    def calculateTotalHours(self, piles, speed):
        totalH = 0
        for bananas in piles:
            totalH += math.ceil(bananas / speed)
        return totalH

    # Function to find minimum eating speed
    def minEatingSpeed(self, piles, h):
        # Find maximum element
        maxPile = max(piles)

        # Initialize low and high pointers
        low, high = 1, maxPile
        ans = maxPile

        # Binary search on answer space
        while low <= high:
            mid = (low + high) // 2
            totalH = self.calculateTotalHours(piles, mid)

            # If possible, try smaller speed
            if totalH <= h:
                ans = mid
                high = mid - 1
            # Otherwise, try larger speed
            else:
                low = mid + 1

        return ans

