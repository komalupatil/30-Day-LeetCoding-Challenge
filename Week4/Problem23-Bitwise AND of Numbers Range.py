#Problem23
#Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.
#Example 1:
#Input: [5,7]
#Output: 4
#Example 2:
#Input: [0,1]
#Output: 0


#Solution1
#right shift the m and n till m < n and increase the count everytime.
#once m <n, left shift the m by count.

class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        count  = 0
         
        while m < n:
            m = m >> 1
            n = n >> 1
            count += 1
        return m << count


#Solution2 - using bitwise AND operator

class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if len(bin(m)) != len(bin(n)):
            return 0
        
        for i in range(m+1, n+1):
            m = m & i
        return m