#Problem18

#Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
#Note: You can only move either down or right at any point in time.
#Example:
#Input:
#[
#  [1,3,1],
#  [1,5,1],
#  [4,2,1]
#]
#Output: 7
#Explanation: Because the path 1→3→1→1→1 minimizes the sum.


#Solution using DP

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return 0
        
        m = len(grid)
        n= len(grid[0])
        
        dp = [[1 for _ in range(n)] for _ in range(m)]
        
        #dp = [[1*len(grid)]*len(grid[0])]
        
        dp[0][0] = grid[0][0]
        
        #first row
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
            
        #first column
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        
        
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = grid[i][j] + min(dp[i][j-1], dp[i-1][j])
                
                
        return dp[len(grid)-1][len(grid[0])-1]