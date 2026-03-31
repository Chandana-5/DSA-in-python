#brutte force
#algorithm
#1.The brute force way is to simply check each element from left to right. If we find the target, we return its index; otherwise, we return -1 after scanning the entire array.
#2.Start a loop from the first element to the last element.
#3.For each element:
#4.Compare it with the target value.
#5.If it matches the target, return the current index immediately.
#6.If the loop finishes and no match is found, return -1.
#time complexity O(N)
#space complexity O(1)
class Solution:
    # Function to search target in rotated sorted array using brute force
    def search(self, nums, target):

        # Loop through each element in the array
        for i in range(len(nums)):

            # If current element matches target, return index
            if nums[i] == target:
                return i

        # If not found, return -1
        return -1
#optimal solutiom
#algorithm
#1.Start by looking at the middle element of the array.
#2.Check if this middle element is the target if yes, return its index immediately.
#3.Now figure out which half of the array (left side or right side) is sorted.
#4.If the left part is sorted:
#5.Check if the target number falls within the range of that sorted part.
#6.If it does, discard the right half and continue the search in the left part.
#7.If it doesn’t, discard the left half and search in the right side.
#8.If the right part is sorted:
#9.Do the same check if the target is in that sorted part.
#10If yes, discard the left side and search in the right.
#11.If not, discard the right and continue with the left.
#12.Repeat this process of eliminating half the array until the target is found or the search space is empty.
#Time Complexity: O(log N)
#Space Complexity: O(1)
class Solution:
    def search(self, nums, target):
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1

