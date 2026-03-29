#Time Complexity:O(logN)
#Space Complexity: O(1)
class FloorCeilFinder:
    def find_floor(self, arr, x):
        low, high = 0, len(arr) - 1
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] <= x:
                ans = arr[mid]  # Potential floor
                low = mid + 1
            else:
                high = mid - 1
        return ans

    def find_ceil(self, arr, x):
        low, high = 0, len(arr) - 1
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] >= x:
                ans = arr[mid]  # Potential ceil
                high = mid - 1
            else:
                low = mid + 1
        return ans

    def get_floor_and_ceil(self, arr, x):
        floor = self.find_floor(arr, x)
        ceil = self.find_ceil(arr, x)
        return floor, ceil
