#Problem 5


#The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
#Given two integers x and y, calculate the Hamming distance.
#Note:
#0 ≤ x, y < 231.
#Example:
#Input: x = 1, y = 4
#Output: 2
#Explanation:
#1   (0 0 0 1)
#4   (0 1 0 0)
#       ↑   ↑
#The above arrows point to positions where the corresponding bits are different.



#SOlution

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x = x ^ y
        y = 0
        while x:
            y += 1 # add (x & 1) here for (x >>1)
            x = x & (x-1) #same as (x >> 1) right shift x by 1
        return y