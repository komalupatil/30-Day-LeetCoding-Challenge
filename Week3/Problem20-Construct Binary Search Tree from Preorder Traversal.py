#Problem20
#Return the root node of a binary search tree that matches the given preorder traversal.
#(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)
#Example 1:
#Input: [8,5,1,7,10,12]
#Output: [8,5,10,1,7,null,12]
#Note: 
#1 <= preorder.length <= 100
#The values of preorder are distinct.


#Solution1 - recursion
#Convert preorder into inorder by sorting it. then find the index root in inorder and do the recursion


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        
        inorder = sorted(preorder)
        
        return self.helper(preorder, inorder)
    
    def helper(self, preorder, inorder):
        
        lengthPre = len(preorder)
        lengthIn = len(inorder)
        
        if lengthPre != lengthIn or preorder == None or inorder==None or lengthPre == 0:
            return None
        
        root = TreeNode(preorder[0])
        rootIndex = inorder.index(root.val)
        
        root.left = self.helper(preorder[1:rootIndex+1], inorder[:rootIndex])
        
        root.right = self.helper(preorder[rootIndex+1:], inorder[rootIndex+1:])
        
        return root


#SOlution2 - Interative approach

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        
        root = TreeNode(preorder[0])
        
        stack = [root]
        
        for value in preorder[1:]:
            if value < stack[-1].val:
                stack[-1].left = TreeNode(value)
                stack.append(stack[-1].left)
            else:
                while stack and stack[-1].val <value:
                    last = stack.pop()
                last.right = TreeNode(value)
                stack.append(last.right)
                
        return root