#brutteforce
#algorithm
#1.Initialize an empty list to store words.
#2.Traverse the string character by character.
#3.Identify consecutive non-space characters as a word.
#4.Ignore extra spaces and leading/trailing spaces while collecting words.
#5.Append each identified word to the list.
#6.Reverse the list of words.
#7.Join the reversed list into a single string using a single space.
#8.Return the resulting string.
#time complexity-O(N)
#space complexity-O(N)
class solution:
  def reverse(self,n):
    words=[]
    word=''
    for char in s:
      if char!='':
        word+=char 
      elif word:
        words.append(word) 
        word='' 
    if word:
      words.append(word) 
      words.reverse()
      return " ".join(words)
#optimal solution
#algorithm
#1.Initialize an empty result string.
#2.Set a pointer at the last character of the string.
#3.While the pointer is within the string:
#4.Skip all spaces to move to the end of a word.
#5.Mark the end position of the word.
#6.Move the pointer backward until a space or start of string is found.
#7.Extract the word and append it to the result string.
#8.If result is not empty, add a space before appending the next word.
#9.Return the result string.
#time complexity-O(N)
#space complexity-0(1)
class Solution:
    def reverseWords(self, s: str) -> str:
        result = ""
        i = len(s) - 1
        while i >= 0:
            while i >= 0 and s[i] == " ":
                i -= 1
            if i < 0:
                break
            end = i
            while i >= 0 and s[i] != " ":
                i -= 1
            
    
            word = s[i + 1:end + 1]
            
    
            if result != "":
                result += " "
            
            result += word
        
        return result

