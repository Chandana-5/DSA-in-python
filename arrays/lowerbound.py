#brutte 
class LowerBoundFinder:
    # Method to find lower bound index
    def lower_bound(self, arr, x):
        for i in range(len(arr)):
            if arr[i] >= x:
                return i  
        return len(arr)  
#optimal
class LowerBoundFinder:
    # Function to find the lower bound index using binary search
    def lower_bound(self, arr, x):
        low, high = 0, len(arr) - 1     
        ans = len(arr)                 

        while low <= high:
            mid = (low + high) // 2     
            if arr[mid] >= x:
                ans = mid               
                high = mid - 1          
            else:
                low = mid + 1           
        return ans
