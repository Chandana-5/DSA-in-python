#brutte
#algorithm
#1.Linear search to find upper bound
#2.First element greater than x
 #3.Return size if no such element found
#time complexity O(N)
#space complexity O(1)

class UpperBoundFinder:
    def upper_bound(self, arr, x):
        for i in range(len(arr)):
            if arr[i] > x:
                return i  
        return len(arr)   
#optimal 
#algorithm
#1.Place the 2 pointers i.e. low and high: Initially, we will place the pointers like this:
#2.low will point to the first index, and high will point to the last index.
#3.Calculate the ‘mid’: Now, we will calculate the value of mid using the following formula:
#4.mid = (low+high) // 2 ( ‘//’ refers to integer division)
#5.Compare arr[mid] with x: With comparing arr[mid] to x, we can observe 2 different cases:
#6.Case 1 - If arr[mid] > x: This condition means that the index mid may be an answer. 
#7.So, we will update the ‘ans’ variable with mid and search in the left half if there is any smaller index that satisfies the same condition.
#8.Here, we are eliminating the right half.
#time complexity-O(logn) 
#space complexity-O(1)
class UpperBoundFinder:
    def upper_bound(self, arr, x):
        low, high = 0, len(arr) - 1
        ans = len(arr)  # Default to length if no element > x

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] > x:
                ans = mid      # Store current mid as answer
                high = mid - 1 # Search left
            else:
                low = mid + 1  # Search right
        return ans
