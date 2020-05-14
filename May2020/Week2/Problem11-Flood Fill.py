#Problem11

#An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).
#Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.
#To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.
#At the end, return the modified image.
#Example 1:
#Input: 
#image = [[1,1,1],[1,1,0],[1,0,1]]
#sr = 1, sc = 1, newColor = 2
#Output: [[2,2,2],[2,2,0],[2,0,1]]
#Explanation: 
#From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected 
#by a path of the same color as the starting pixel are colored with the new color.
#Note the bottom corner is not colored 2, because it is not 4-directionally connected
#to the starting pixel.
#Note:
#The length of image and image[0] will be in the range [1, 50].
#The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
#The value of each color in image[i][j] and newColor will be an integer in [0, 65535].


#Solution 

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image == None:
            return None
        
        self.dfs(image,sr,sc,newColor,image[sr][sc])
        
        return image
    
    def dfs(self, image,i,j,newColor,currentColor):
        if i<0 or j<0 or i>=len(image) or j>=len(image[0]):
            return image
        if image[i][j] == newColor:
            return image
        
        if image[i][j] != currentColor:
            return image
        
        image[i][j] = newColor
        
        self.dfs(image,i,j-1,newColor,currentColor)
        self.dfs(image,i,j+1,newColor,currentColor)
        self.dfs(image,i-1,j,newColor,currentColor)
        self.dfs(image,i+1,j,newColor,currentColor)