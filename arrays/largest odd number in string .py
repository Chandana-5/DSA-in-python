#brutte
#algorithm
#1.Initialize an empty result string to store the processed output
#2.Initialize a counter (level) to track the depth of parentheses
#3.Traverse through the string character by character:
#4.If the current character is '(', increment the level counter. If the level is greater than 1 (indicating we're inside a valid primitive), add '(' to the result string
#5.If the current character is ')', decrement the level counter. If the level is greater than 0 (indicating we're still inside a valid primitive), add ')' to the result string
#6.After the entire string has been traversed, return the result string
#time complexity o(n)
#space complexity o(1)
class Solution:
    # Function to find the largest odd number that is a substring of given string 
    def largeOddNum(self, s: str) -> str:
        ind = -1
        
        # Iterate through the string from the end to beginning
        i = 0
        for i in range(len(s) - 1, -1, -1):
            # Break if an odd digit is found
            if (int(s[i]) % 2) == 1:
                ind = i
                break
        
        # Skipping any leading zeroes
        i = 0
        while i <= ind and s[i] == '0':
            i += 1
        
        # Return the largest odd number substring
        return s[i:ind + 1]
