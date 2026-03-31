#brutte
#algorithm
#1.Find the total size of the array.
#2.If the size is equal to one, return the only element.
#3.Traverse the array from start to end.
#4.If the current element is the first one, compare it with the next. If they are different, return it.
#5.If the current element is the last one, compare it with the previous. If they are different, return it.
#6.Otherwise, compare the current element with both previous and next. If it is different from both, return it.
#7.If no such element is found during traversal, return an invalid marker (though by problem guarantee, one will always exist).
#time complexity O(N)
#space complexity O(1)
class Solution:
    def singleNonDuplicate(self, arr):
        n = len(arr)
        if n == 1:
            return arr[0]
        for i in range(n):
            if i == 0:
                if arr[i] != arr[i + 1]:
                    return arr[i]
            elif i == n - 1:
                if arr[i] != arr[i - 1]:
                    return arr[i]
            else:
                if arr[i] != arr[i - 1] and arr[i] != arr[i + 1]:
                    return arr[i]
        return -1
#optimal approach
#algorithm
#1.Check if the array has only one element, return that element.
#2.Check if the first element is not equal to the second return the first.
#3.Check if the last element is not equal to the second last return the last.
#4.Set two pointers: low = 1, high = n - 2 (excluding boundary elements).
#5.Run a loop while low ≤ high:
#6.Find mid = (low + high) / 2.
#6.If arr[mid] ≠ arr[mid - 1] and arr[mid] ≠ arr[mid + 1], return arr[mid].
#7.Check if mid is part of a correct pair:
#8.If mid is even and arr[mid] == arr[mid + 1], or
#9.If mid is odd and arr[mid] == arr[mid - 1],
#10.Then the unique element lies to the right, so move low = mid + 1.
#11.Otherwise, move high = mid - 1.
#12.If no unique element is found (theoretically unreachable), return -1.
#time complexity O(N log N)
#space complexityO(1)
class Solution:
    def singleNonDuplicate(self, arr):
        n = len(arr)
        if n == 1:
            return arr[0]
        if arr[0] != arr[1]:
            return arr[0]
        if arr[n - 1] != arr[n - 2]:
            return arr[n - 1]
        low, high = 1, n - 2
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] != arr[mid + 1] and arr[mid] != arr[mid - 1]:
                return arr[mid]
            if (mid % 2 == 1 and arr[mid] == arr[mid - 1]) or \
               (mid % 2 == 0 and arr[mid] == arr[mid + 1]):
                low = mid + 1
            else:
                high = mid - 1

        return -1

