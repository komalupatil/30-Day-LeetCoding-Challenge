#Problem3

#Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.
#Each letter in the magazine string can only be used once in your ransom note.
#Note:
#You may assume that both strings contain only lowercase letters.
#canConstruct("a", "b") -> false
#canConstruct("aa", "ab") -> false
#canConstruct("aa", "aab") -> true


#Solution1

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        letters = {}
        for letter in magazine:
            if letter in letters:
                letters[letter] +=1
            else:
                letters[letter] = 1
        for letter in ransomNote:
            if letter in letters:
                letters[letter] -=1
                if letters[letter] == 0:
                    del letters[letter]
            else:
                return False
        return True

#Soltuion2 using set() and count()

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        for i in set(ransomNote):
            if ransomNote.count(i) > magazine.count(i):
                return False
        return True