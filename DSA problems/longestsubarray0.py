#brutte forec
#algorithm
#1.Initialize a variable max = 0, which stores the length of the longest subarray with a sum of 0.
#2.Traverse the array from the start and initialize a variable sum = 0, which stores the sum of the subarray starting with the current index.
#3.Traverse from the next element of the current index up to the end of the array. Each time, add the element to the sum and check if it is equal to 0.
#4.If sum = 0, check if the length of the subarray so far is greater than max, and if yes, update max.
#5.Continue adding elements and repeat the above step until the outer loop completes traversing all elements.
#6.Finally, return the max which holds the length of the longest subarray with a sum of 0.
#time complexity O(N^2)
#space complexity O(1)
def solve(a: list[int]) -> int:
    max_len = 0
    
    sum_index = {}
    s = 0

    for i, val in enumerate(a):
        s += val
        if s == 0:
            max_len = i + 1
        elif s in sum_index:
            max_len = max(max_len, i - sum_index[s])
        else:
            sum_index[s] = i
    return max_len
  #optimal solution
#algorithm
#1.Initialize a variable sum = 0, which stores the sum of elements traversed so far, and another variable max = 0, which stores the length of the longest subarray with sum zero.
#2.Declare a HashMap<Integer, Integer> to store the prefix sum of every element as a key and its index as a value.
#3.Traverse the array and add the array element to the sum.
#4.If sum = 0, update max with the maximum value between max and current_index + 1, as the subarray from the start to the current index has a sum of 0.
#5.If sum is not equal to zero, check the HashMap to see if we've encountered this sum before.
#6.If the HashMap contains the sum, this indicates that a subarray with the same sum exists, so update max accordingly.
#6.If the sum is not found in the HashMap, insert (sum, current_index) into the HashMap to store the prefix sum until the current index.
#7.After traversing the entire array, the max variable will hold the length of the longest subarray with a sum equal to zero. Return max.
#time complexity O(n)
#space complexity O(1)
def maxLen(A: list[int], n: int) -> int:
    mpp: dict[int, int] = {}
    maxi = 0
    s = 0
    for i in range(n):
        s += A[i]
        if s == 0:
            maxi = i + 1
        else:
            if s in mpp:
                maxi = max(maxi, i - mpp[s])
            else:
                mpp[s] = i

    return maxi
