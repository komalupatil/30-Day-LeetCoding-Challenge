#Problem27

#Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
#Example:
#Input: 
#1 0 1 0 0
#1 0 1 1 1
#1 1 1 1 1
#1 0 0 1 0
#Output: 4


#Solution

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m= len(matrix)   
        if m == 0:
            return 0
        n= len(matrix[0])
        
        height = 0
        
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if matrix[i-1][j-1] == "1":
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                    height = max(height, dp[i][j])
        return height**2