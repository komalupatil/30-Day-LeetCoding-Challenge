#Problem 16
#Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:
#Any left parenthesis '(' must have a corresponding right parenthesis ')'.
#Any right parenthesis ')' must have a corresponding left parenthesis '('.
#Left parenthesis '(' must go before the corresponding right parenthesis ')'.
#'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
#An empty string is also valid.
#Example 1:
#Input: "()"
#Output: True
#Example 2:
#Input: "(*)"
#Output: True
#Example 3:
#Input: "(*))"
#Output: True
#Note:
#The string size will be in the range [1, 100].

#Solution - Greedy Approach

class Solution:
    def checkValidString(self, s: str) -> bool:
        if len(s) == 0:
            return True
        left_count = 0
        right_count = 0
        for i in range(len(s)):
            left_count +=1 if s[i] in "(*" else -1
            right_count +=1 if s[len(s)-i-1] in ")*" else -1
            if left_count < 0 or right_count < 0:
                return False
    
        return True