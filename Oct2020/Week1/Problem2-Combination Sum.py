#Problem 2

#Leetcode 39. Combination Sum

#Solution 

class Solution:    
    def dfs(self, subset, index, candidates, current, target):
        if target <0:
            return
        
        elif target == 0:
            subset.append(current[:])
            return
        
        for i in range(index, len(candidates)):
            current.append(candidates[i])
            self.dfs(subset, i, candidates, current, target-candidates[i])
            current.pop()
            
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        subset = []
        self.dfs(subset, 0,candidates, [], target)
        return subset
                