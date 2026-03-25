#brutte
#algorithm 
#1.Initialize a counter to 0 for storing the number of valid subarrays.
#2.Loop through each index i as the starting point of the subarray.
#3.Set a variable xor = 0 for maintaining the running XOR of the current subarray.
#4.Loop through each index j from i to n-1 to extend the subarray.
#5.Update xor by taking xor = xor ^ A[j].
#6.If xor equals B, increment the counter by 1.
#7.After all iterations, return the counter as the total number of subarrays.
#time complexityO(N^2)
#Space Complexity: O(1) 
class Solution:
    def countSubarraysXOR(self, A, B):
        count = 0
        for i in range(len(A)):
            xorVal = 0
            for j in range(i, len(A)):
                xorVal ^= A[j]
                if xorVal == B:
                    count += 1
        return count
#optimal
#algorithm
#1.Initialize a hashmap to store how many times each prefix XOR has appeared.
#2.Keep a variable to store the current prefix XOR as we move through the array.
#3.Keep another variable to count the total number of subarrays with XOR equal to k.
#4.For each element in the array, update the prefix XOR by combining it with the current element.
#5.If the prefix XOR itself is equal to k, increase the count by one.
#6.Check if there exists a prefix XOR seen before that can make the subarray XOR equal to k, and if yes, add its frequency from the hashmap to the count.
#7.Store or update the frequency of the current prefix XOR in the hashmap.
#8.After processing all elements, the count will be the total number of subarrays with XOR equal to k.
#time complexity O(N),
#space complexity O(N)
    class Solution:
    def countSubarrays(self, A, k):
        freq = {0: 1}
        prefixXor = 0
        count = 0
        for num in A:
            prefixXor ^= num
            target = prefixXor ^ k

    
            if target in freq:
                count += freq[target]
            freq[prefixXor] = freq.get(prefixXor, 0) + 1

        return count

