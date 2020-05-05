#Problem5
#Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
#Examples:
#s = "leetcode"
#return 0.
#s = "loveleetcode",
#return 2.
#Note: You may assume the string contain only lowercase letters.


#Solution

class Solution:
    def firstUniqChar(self, s: str) -> int:
        if s == "":
            return -1
        
        d = {}
        
        for char in s:
            if char not in d:
                d[char] = 1
            else:
                d[char] += 1
        for i,char in enumerate(s):
            if d[char] == 1:
                #return first unique character
                return i
        return -1