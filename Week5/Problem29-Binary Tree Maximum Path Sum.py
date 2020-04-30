#Problem29
#Given a non-empty binary tree, find the maximum path sum.
#For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.
#Example 1:
#Input: [1,2,3]

       1
      / \
     2   3
#Output: 6
#Example 2:
#Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7
#Output: 42


#Solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
    
        self.maxpathSum = float('-inf')
        
        def depth(node):
            
            if node == None:
                return 0
            
            left = max(0, depth(node.left))
            right = max(0, depth(node.right))
            currentmaxPath=node.val+left+right
            self.maxpathSum = max(self.maxpathSum, currentmaxPath)

            return (max(left,right) + node.val)
        depth(root)
        return self.maxpathSum