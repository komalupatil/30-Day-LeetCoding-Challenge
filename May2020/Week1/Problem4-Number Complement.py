#Problem4

#Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.
#Example 1:
#Input: 5
#Output: 2
#Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
#Example 2:
#Input: 1
#Output: 0
#Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0


#Solution 

class Solution:
    def findComplement(self, num: int) -> int:
        temp = num
        bit = 1
        while temp != 0:
            #xor of num with 1, each digit at a time
            num = num ^ bit
            #need to shift bit to take xor each time with other digit
            bit = bit << 1
            #to know when to stop shifting bit to the left, we also need to shift num (temp)
            temp = temp >> 1
        return num
            