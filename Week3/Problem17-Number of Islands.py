#Problem17

#Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
#Example 1:
#Input:
#11110
#11010
#11000
#00000
#Output: 1
#Example 2:
#Input:
#11000
#11000
#00100
#00011
#Output: 3

#Solution 

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0
        noOfIslands = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][i] == '1':
                    self.dfs(grid,i,j)
                    noOfIslands +=1
        return noOfIslands
        
    def dfs(self,grid,i,j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]):
            return
        if grid[i][j] != '1':
            return 
        
        grid[i][j] = '0'
        self.dfs(grid,i+1,j)
        self.dfs(grid,i-1,j)
        self.dfs(grid,i,j-1)
        self.dfs(grid,i,j+1)

