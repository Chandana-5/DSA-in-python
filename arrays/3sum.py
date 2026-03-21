#brutte force
#algorithm
#1.use a set because we need only unique triplets
#2.run the first loop from the start to end of array
#3.inside it run second loop from next position to end
#4.run third loop from next position after second loop to end
#5.for every three numbers check if their sum equals to 0 . if yes sort triplet and add it to set
#6.at end return all triplets from the set
#time complexity O(N^3)
#space complexity O(2*no of unique triplets)
# Class to solve 3-sum problem
class Solution:
    def threeSum(self, arr, n):
        # Store unique triplets
        st = set()

        for i in range(n):
            # Second loop for second element
            for j in range(i + 1, n):
                # Third loop for third element
                for k in range(j + 1, n):
                    # If triplet sum is zero
                    if arr[i] + arr[j] + arr[k] == 0:
                        # Store sorted triplet to avoid duplicates
                        triplet = tuple(sorted([arr[i], arr[j], arr[k]]))
                        st.add(triplet)
        return [list(triplet) for triplet in st
    #better solution
  #algorithm
  #1.store unique triplets
  #2.first loop for first element
  #2.set to store elements seen in this iteration
  #3.second loop for second element
  #4.calculate third element needed
  #5.if third already in set, we found triplet
  #6.add current element to set
  #7.convert set to list of lists
  #8.time complexity O(N2 * log(no. of unique triplets))
  #space complexity O(2 * no. of the unique triplets) + O(N)
class Solution:
    def threeSum(self, arr, n):
        ans = set()
        for i in range(n):
            hashset = set()
            for j in range(i + 1, n):
                third = -(arr[i] + arr[j])
                if third in hashset:
                    triplet = tuple(sorted([arr[i], arr[j], third]))
                    ans.add(triplet)
                hashset.add(arr[j])
        return [list(triplet) for triplet in ans
  #optimal approach
  #algorithm 
  #1.sort the array
  #2.store final result 
  #3.first loop for first element
  #4.skip duplicates for first element
  #5.two pointers left,right
  #6.find pairs for current arr[i]
  #7.skip duplicates for left and right 
  #time complexity  O(NlogN)+O(N2)
  #space complexity O(no. of quadruplets)
class Solution:
    def threeSum(self, arr, n):
        arr.sort()
        ans = []
        for i in range(n):
            if i > 0 and arr[i] == arr[i - 1]:
                continue
            left, right = i + 1, n - 1
            while left < right:
                total = arr[i] + arr[left] + arr[right]

                if total == 0:
                    ans.append([arr[i], arr[left], arr[right]])
                    left += 1
                    right -= 1
                    while left < right and arr[left] == arr[left - 1]:
                        left += 1
                    while left < right and arr[right] == arr[right + 1]:
                        right -= 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return ans
