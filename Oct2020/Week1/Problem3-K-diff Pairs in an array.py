#Problem 3

#Leetcode 532. K-diff Pairs in an Array

#Solution 1 - using hashmap
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        hashmap = {}
        result = set()
        #{3:0, 1:1, 4:2, 1:3, 5:4}
        #[3,1,4,1,5]
        
        for i, num in enumerate(nums):
            hashmap[num] = i
            
        for j,num in enumerate(nums):
            if num-k in hashmap and (num, num-k) not in result and hashmap[num-k] != j:
                result.add((num,num-k))
        return len(result)



#Solution 2 TLE error
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        ans = 0
        
        for i in range(len(nums)):
            if i> 0 and nums[i] == nums[i-1]:
                continue
            
            for j in range(i+1, len(nums)):
                if j>i+1 and nums[j] == nums[j-1]:
                    continue
                if abs(nums[i]-nums[j]) == k:
                    ans += 1
        return ans