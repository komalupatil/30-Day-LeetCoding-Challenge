#Problem8
#You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.
#Example 1:
#Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
#Output: true
#Example 2:
#Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
#Output: false
#Constraints:
#2 <= coordinates.length <= 1000
#coordinates[i].length == 2
#-10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
#coordinates contains no duplicate point.


#Solution

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 2:
            return True
        
        (x0, y0), (x1,y1) = coordinates[:2]
        for x, y in coordinates:
            #in 3 pts given, 
            # slope between 1st and 2nd and 2nd 
            # and 3rd must be equal to be a straight line
            if (y1-y0)*(x-x1) != (y-y1)*(x1-x0):
                return False
        return True