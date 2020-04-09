#Problem9

#Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.
#Example 1:
#Input: S = "ab#c", T = "ad#c"
#Output: true
#Explanation: Both S and T become "ac".
#Example 2:
#Input: S = "ab##", T = "c#d#"
#Output: true
#Explanation: Both S and T become "".
#Example 3:
#Input: S = "a##c", T = "#a#c"
#Output: true
#Explanation: Both S and T become "c".
#Example 4:
#Input: S = "a#c", T = "b"
#Output: false
#Explanation: S becomes "c" while T becomes "b".
#Note:
#1 <= S.length <= 200
#1 <= T.length <= 200
#S and T only contain lowercase letters and '#' characters.
#Follow up:
#Can you solve it in O(N) time and O(1) space?



#Solution 


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        indexS, indexT = len(S)-1, len(T)-1
        countS = countT = 0
        while indexS >=0 or indexT >=0:
            
            while indexS >=0:
                
                if S[indexS] == "#":
                    countS +=1
                    indexS -=1
                elif countS >0:
                    countS -=1
                    indexS -=1
                else:
                    break
        
        
            while indexT >=0:
                
                if T[indexT] == "#":
                    countT +=1
                    indexT -=1
                elif countT >0:
                    countT -=1
                    indexT -=1
                else:
                    break
            
            if indexS < 0  and indexT <0:
                return True
            
            if indexS < 0  or indexT <0:
                    return False
                
            if S[indexS] != T[indexT]:
                return False
                    
            
            indexS -=1
            indexT -=1
            
        return True
                