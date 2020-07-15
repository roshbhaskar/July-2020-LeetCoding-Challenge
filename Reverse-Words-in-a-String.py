'''
Given an input string, reverse the string word by word.

Example 1:

Input: "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: "  hello world!  "
Output: "world! hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split()
        s.reverse()
        new_s=''
        for i in s:
            new_s= new_s+ i+' '
        cut = len(new_s)
        return new_s[0:cut-1]    
        
