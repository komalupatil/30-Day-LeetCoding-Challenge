#Problem 20
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

 

#Example 1:
#Input: root = [3,1,4,null,2], k = 1
#   3
#  / \
# 1   4
#  \
#   2
#Output: 1

#Example 2:
#Input: root = [5,3,6,2,4,null,null,1], k = 3
#       5
#      / \
#     3   6
#    / \
#   2   4
#  /
# 1
#Output: 3

#Follow up:
#What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

#Constraints:
#The number of elements of the BST is between 1 to 10^4.
#You may assume k is always valid, 1 ≤ k ≤ BST's total elements.



#Solution1 - use inorder since it gives sorted result

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        
        def in_order(root):
            if root== None:
                return []
            in_left = in_order(root.left)
            root_val = [root.val]
            in_right = in_order(root.right)
            print(in_left + root_val + in_right)
            return in_left + root_val + in_right
        return in_order(root)[k-1]



#Solution2

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.k=k
        self.res= None
        self.helper(root)
        return self.res
        
    def helper(self, root):
        if root == None:
            return
        self.helper(root.left)
        self.k -= 1
        if self.k == 0:
            self.res=root.val
            return
        self.helper(root.right)