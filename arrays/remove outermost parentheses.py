#brutte
#algorithm
#1. an empty result string to store the processed output
#2.Initialize a counter (level) to track the depth of parentheses
#3.Traverse through the string character by character:
#4.If the current character is '(', increment the level counter. If the level is greater than 1 (indicating we're inside a valid primitive), add '(' to the result string
#5.If the current character is ')', decrement the level counter. If the level is greater than 0 (indicating we're still inside a valid primitive), add ')' to the result string
#6.After the entire string has been traversed, return the result string
#time complexity o(n)
#space complexity o(1)
class Solution:
    def removeOuterParentheses(self, nums):
        result = ""  
        level = 0     
        for char in s:
            if char == '(':
                if level > 0:
                    result += char
                level += 1  
            elif char == ')':
                level -= 1  
                if level > 0:
                    result += char
        return result


# Get result
