#brutte force
#algorithm
#1.First, we will find the maximum element and the summation of the given array.
#2.We will use a loop(say time) to check all possible answers from max(arr[]) to sum(arr[]).
#3.Next, inside the loop, we will send ‘time’, to the function countPainters() function to get the number of painters to whom we can allocate the boards.
#4.The first value of ‘time’, for which the number of painters will be lesser or equal to ‘k’, will be our answer. So, we will return that particular value of ‘time’.
#5.Finally, if we are out of the loop, we will return max(arr[]) as there cannot exist any answer smaller than that.
#time complexity-O(N * (sum(arr[])-max(arr[])+1))
#space complexity-O(1) 
from typing import List

class PainterPartition:
    def count_painters(self, boards: List[int], time: int) -> int:
        painters = 1             
        boards_painter = 0        

        for board in boards:
            if boards_painter + board <= time:
                boards_painter += board
            else:
                # Assign board to a new painter
                painters += 1
                boards_painter = board

        return painters
    def find_largest_min_distance(self, boards: List[int], k: int) -> int:
        low = max(boards)        
        high = sum(boards)     

        for time in range(low, high + 1):
            if self.count_painters(boards, time) <= k:
                return time      

        return low  
#optimal approach
#algorithm
#1.Place the 2 pointers i.e. low and high: Initially, we will place the pointers. The pointer low will point to max(arr[]) and the high will point to sum(arr[]).
#2.Calculate the ‘mid’: Now, inside the loop, we will calculate the value of ‘mid’ using the following formula: mid = (low+high) // 2 ( ‘//’ refers to integer division.
#3.Eliminate the halves based on the number of painters returned by countPainters(): We will pass the potential value of time, represented by the variable 'mid', to the ‘countPainters()' function. This function will return the number of painters we need to paint all the boards
#4.If painters > k: On satisfying this condition, we can conclude that the number ‘mid’ is smaller than our answer. So, we will eliminate the left half and consider the right half(i.e. low = mid+1).
#5.Otherwise, the value mid is one of the possible answers. But we want the minimum value. So, we will eliminate the right half and consider the left half(i.e. high = mid-1).
#6.Finally, outside the loop, we will return the value of low as the pointer will be pointing to the answer.
Code
#time complexity-O(N * log(sum(arr[])-max(arr[])+1))
#space complexity-O(1)
from typing import List

class PainterPartition:
    def count_painters(self, boards: List[int], time: int) -> int:
        painters = 1
        boards_painter = 0

        for board in boards:
            if boards_painter + board <= time:
                boards_painter += board
            else:
                painters += 1
                boards_painter = board

        return painters

    def find_largest_min_distance(self, boards: List[int], k: int) -> int:
        low = max(boards)
        high = sum(boards)
        result = high

        while low <= high:
            mid = (low + high) // 2
            painters = self.count_painters(boards, mid)

            if painters > k:
                low = mid + 1  
            else:
                result = mid  
                high = mid - 1

        return result

