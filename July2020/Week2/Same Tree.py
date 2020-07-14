#Problem 13

#Given two binary trees, write a function to check if they are the same or not.
#Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
#Example 1:
#Input:     1         1
#          / \       / \
#         2   3     2   3

#        [1,2,3],   [1,2,3]
#Output: true

#Example 2:
#Input:     1         1
#          /           \
#         2             2

#        [1,2],     [1,null,2]
#Output: false

#Example 3:
#Input:     1         1
#          / \       / \
#         2   1     1   2

#        [1,2,1],   [1,1,2]
#Output: false


#Solution - Iterative


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        stack = []
        stack.append((p, q))
        
        while stack:
            
            node1, node2 = stack.pop(0)
              
            if node1==None and node2==None:
                continue
            
            if node1 == None and node2 is not None:
                return False
            
            if node1 is not None and node2 is None:
                return False
            
            if node1.val != node2.val:
                return False
            
            stack.append((node1.left, node2.left))
            stack.append((node1.right, node2.right))
            
                     
        return True


#Solution - Recursive


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        
        if p is None and q is not None:
            return False
        
        if p is not None and q is None:
            return False
        
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)