#Problem22

#Given a string, sort it in decreasing order based on the frequency of characters.

#Example 1:
#Input:
#"tree"
#Output:
#"eert"
#Explanation:
#'e' appears twice while 'r' and 't' both appear once.
#So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

#Example 2:
#Input:
#"cccaaa"
#Output:
#"cccaaa"
#Explanation:
#Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
#Note that "cacaca" is incorrect, as the same characters must be together.

#Example 3:
#Input:
#"Aabb"
#Output:
#"bbAa"
#Explanation:
#"bbaA" is also a valid answer, but "Aabb" is incorrect.
#Note that 'A' and 'a' are treated as two different characters.

#Solution - using hash map and bucket sort

class Solution:
    def frequencySort(self, s: str) -> str:
        if len(s) == 0:
            return ""
        
        d = {}
        
        for char in s:
            if char in d:
                d[char] += 1
            else:
                d[char] = 1
                
        buckets = [[] for _ in s]
        
        for key,value in d.items():
            buckets[value-1].append(key*value)
        
        res = ""
        
        for bucket in buckets[::-1]:
            if len(bucket):
                
                for char in bucket[::-1]:
                    res += char
        return res        
        

#Solution2

class Solution:
    def frequencySort(self, s: str) -> str:
        if len(s) == 0:
            return ""
        
        d = {}
        
        for char in s:
            if char in d:
                d[char] += 1
            else:
                d[char] = 1
                
        s_new = sorted(d, key=lambda x: d[x], reverse=True)
        res = ""
        for char in s_new:
            res += char*d[char]
            
        return res