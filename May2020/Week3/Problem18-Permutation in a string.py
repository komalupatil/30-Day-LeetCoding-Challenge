#problem18

#Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.
#Example 1:
#Input: s1 = "ab" s2 = "eidbaooo"
#Output: True
#Explanation: s2 contains one permutation of s1 ("ba").
#Example 2:
#Input:s1= "ab" s2 = "eidboaoo"
#Output: False
 
#Note:
#The input strings only contain lower case letters.
#The length of both given strings is in range [1, 10,000].


#Solution

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        length_of_s1  = len(s1)
        s1_counter = Counter(s1)
        window_counter = Counter()
        
        for i,ch in enumerate(s2):
            window_counter[ch] +=1
            
            if i>= length_of_s1:
                eliminate_from_left = s2[i-length_of_s1]
            
                if window_counter[eliminate_from_left] == 1:
                    del window_counter[eliminate_from_left]
                else:
                    window_counter[eliminate_from_left] -=1
            
            if window_counter == s1_counter:
                return True
        return False

