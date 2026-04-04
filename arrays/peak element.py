#brutte force
#algorithm
#A peak element in an array refers to the element that is greater than both of its neighbors.
#Basically, if arr[i] is the peak element, arr[i] > arr[i-1] and arr[i] > arr[i+1].
#time complexity O(N)
#space complexity O(1)
class Solution:
    def findPeakElement(self, nums):
        n = len(nums)
        for i in range(n):
            left = (i == 0) or (nums[i] >= nums[i - 1])
            right = (i == n - 1) or (nums[i] >= nums[i + 1])
            if left and right:
                return i
        return -1
#optimal 
#algorithm
#1.Initialize the search space to the full range of the array.
#2.Find the middle index of the current search range.
#3.Check if the middle element is greater than its right neighbor.
#4.If yes, then a peak must exist in the left half (including mid), so shrink the right bound.
#5.Otherwise, the peak must lie in the right half (excluding mid), so shift the left bound.
#6.Continue until the search space converges to a single element.
#7.This final position is the index of a peak element.
#time complexity O(log N)
#space complexity O(1)
class Solution:
    def findPeakElement(self, nums):
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) // 2

            if nums[mid] > nums[mid + 1]:
                high = mid
            else:
                low = mid + 1
        return low
