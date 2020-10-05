#Problem 4

#Leetcode 
#Leetcode 1288. Remove Covered Intervals

#Solution 1

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        
        l = len(intervals)
        r = 0
        
        a, b = intervals[0][0], intervals[0][1]
        
        for i in range(1, l):
            if a <= intervals[i][0] and b >=intervals[i][1]:
                r += 1
            
            elif a == intervals[i][0] and b <intervals[i][1]:
                r += 1
                b = intervals[i][1]
            else:
                a = intervals[i][0]
                b = intervals[i][1]
                
        return l-r


#Solution 2


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        
        merge = []
        
        for interval in intervals:
            if not merge:
                merge.append(interval)
            elif merge[-1][1] < interval[1]:
                if merge[-1][0] < interval[0]:
                    merge.append(interval)
                else:
                    merge[-1] = interval
            else:
                continue
        return len(merge)



#Solution 3

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        
        cur_int = intervals[0]
        
        overlap = 0
        
        for i in range(1, len(intervals)):
            if (cur_int[0] <= intervals[i][0] and cur_int[1] >= intervals[i][1]) or (cur_int[0] >= intervals[i][0] and cur_int[1] <= intervals[i][1]):
                overlap +=1
                cur_int[0] = min(cur_int[0], intervals[i][0])
                cur_int[1] = max(cur_int[1], intervals[i][1])
            else:
                cur_int = intervals[i]
        return len(intervals) - overlap