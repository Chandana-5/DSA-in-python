#brutte
#algorithm
#1.First, we will run a loop(say i) from 0 to N-1 to select the a[i].
#2.As index j should be greater than index i, inside loop i, we will run another loop i.e. j from i+1 to N-1, and select the element a[j].
#3.Inside this second loop, we will check if a[i] > 2*a[j] i.e. if a[i] and a[j] can be a pair. If they satisfy the condition, we will increase the count by 1.
#4.Finally, we will return the count i.e. the number of such pairs.
#time complexity O(N2) 
#space complexity O(1) 
class sloution:
    def reversepair(self,nums):
        n=len(nums)
        cnt=0
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]>2*nums[j]:
                    cnt+=1 
        return cnt  
#optimal approach 
#algorithm
#The merge function works by comparing two elements from two halves i.e. arr[left] and arr[right]. 
#Now, the condition in the question was arr[i] > arr[j]. That is why we merged the logic.
#While comparing the elements, we counted the number of pairs.
#But in this case, the condition is arr[i] > 2*arr[j]. 
#And, we cannot change the condition of comparing the elements in the merge() function. 
#If we change the condition, the merge() function will fail to merge the elements. 
#So, we need to check this condition and count the number of pairs separately.
#time complexity O(2N*logN) 
#space complexity O(N) 
from typing importing list
def merge(nums,low,mid,high):
    temp=[]
    left=low 
    right=mid+1 
    while left<=mid and right<=high:
        if nums[left]<nums[right]:
            temp.append(nums[left])
            left+=1 
        else:
            temp.append(nums[right])
            right+=1 
    while left<=mid:
        temp.append(nums[left])
        left+=1
    while right<=high:
        temp.append(nums[right])
        right+=1 
    for i in range(low,high+1):
        nums[i]=temp[i-low] 
def countpairs(nums,low,mid,high):
    right=mid+1
    cnt=0 
    for i in range(low,mid+1):
        while right<high and nums[left]>2*nums[right]:
            right+=1
        cnt+=(right-(mid+1))
    return cnt 
def mergeSort(arr, low, high):
    cnt = 0
    if low >= high:
        return cnt
    mid = (low + high) // 2
    cnt += mergeSort(arr, low, mid)  # left half
    cnt += mergeSort(arr, mid + 1, high)  # right half
    cnt += countPairs(arr, low, mid, high)  # Modification
    merge(arr, low, mid, high)  # merging sorted halves
    return cnt
