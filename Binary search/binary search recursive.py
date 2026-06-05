class Solution:
    # Recursive Binary Search function
    def binarySearch(self, nums: [int], low: int, high: int, target: int) -> int:
        if low > high:
            return -1  # Base case: target not found

        # Find middle index
        mid = (low + high) // 2

        # If target is found at mid
        if nums[mid] == target:
            return mid
        # If target is greater, search right half
        elif target > nums[mid]:
            return self.binarySearch(nums, mid + 1, high, target)
        # Otherwise, search left half
        return self.binarySearch(nums, low, mid - 1, target)

    # Public function to initiate search
    def search(self, nums: [int], target: int) -> int:
        return self.binarySearch(nums, 0, len(nums) - 1, target)




Complexity Analysis
