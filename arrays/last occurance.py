#brutte
#algorithm
#1.Start traversing the array from the back using a for loop, starting from the last index and moving towards the first.
#2.Check if the current element matches the target element.
#3.If the target element is found, break out of the loop and print the resulting index where the target was found.
#4.If the target element is not found after traversing the entire array, print -1 to indicate that the element is not present.
#time complexity O(N)
#space complexity O(1)
def solve(n: int, key: int, v: list[int]) -> int:
    res = -1
    for i in range(n - 1, -1, -1):
        if v[i] == key:
            res = i
            break
    return res
  #optimal
  #algorithm
  #1.Given that the array is sorted, we can use binary search to efficiently search for the target element.
#2.Initially, set two pointers: start = 0 and end = n-1, where n is the size of the array. Also, initialize the result variable to -1.
#3.While start is less than or equal to end, compute the mid index as mid = (start + end) / 2.
#4.Check if the mid element is equal to the target key:
#5.If they are equal, store the mid value in the result and move the start pointer to mid + 1 to continue searching in the right half.
#6.If the key value is less than the mid element, update the end pointer to mid - 1 to search the left half.
#7.If the key value is greater than the mid element, update the start pointer to mid + 1 to search the right half.
#8.Repeat the process until the start pointer crosses the end pointer or the element is found.
#9.If the element is found, the result will store its index, otherwise, it will remain -1 indicating that the target is not present in the array.
#time complexity O(log N)
#space complexity O(1)
# find last index of key using binary search
def solve(n: int, key: int, v: list[int]) -> int:
    start, end, res = 0, n - 1, -1
    while start <= end:
        mid = start + (end - start) // 2
        if v[mid] == key:
            res = mid
            start = mid + 1
        elif key < v[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return res
