#Problem22
#Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.
#Example 1:
#Input:nums = [1,1,1], k = 2
#Output: 2
#Note:
#The length of the array is in range [1, 20,000].
#The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

#Solution 

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        count,contSum = 0, 0
        
        d = {}
        d[0] = 1 #taking this as contiguous sum start with 0
        
        for i in range(len(nums)):
            contSum += nums[i]
            if contSum-k in d:
                count += d[contSum-k]
            if contSum in d:
                d[contSum] +=1
            else:
                d[contSum] = 1
            
                
        return count    