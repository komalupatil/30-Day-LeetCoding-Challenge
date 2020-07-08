#Problme 7

#You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.
#Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).
#The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

#Input:
#[[0,1,0,0],
# [1,1,1,0],
# [0,1,0,0],
# [1,1,0,0]]
#Output: 16


#Solution

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        result = 0
        if len(grid)==0:
            return None
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                #island found
                if grid[i][j] == 1:
                    result +=4
                    #once island is found make reuslt = 4 as perimeter and then check sides of that island to reduce 1 from reuslt
                #check up 
                    if (i>0 and grid[i-1][j]==1):
                        result -=1
                    #down
                    if(i<(len(grid))-1 and grid[i+1][j]==1):
                        result -=1
                    #left
                    if (j>0 and grid[i][j-1]==1):
                        result -=1
                    #right
                    if (j<len(grid[0])-1 and grid[i][j+1]==1):
                        result -=1
        return result