#Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#Example:
#Input: [0,1,0,3,12]
#Output: [1,3,12,0,0]
#Note:
#You must do this in-place without making a copy of the array.
#Minimize the total number of operations.


#Solution

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = -1
        right = 0
        while right < len(nums):
            if nums[right] == 0:
                right +=1
            else:
                left +=1
                nums[left] = nums[right]
                right +=1
        for i in range(left+1, len(nums)):
            nums[i] = 0
        return nums