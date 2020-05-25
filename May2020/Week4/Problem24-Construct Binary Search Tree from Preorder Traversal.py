#Problem 24

#Return the root node of a binary search tree that matches the given preorder traversal.
#(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)
#It's guaranteed that for the given test cases there is always possible to find a binary search tree with the given requirements.

#Input: [8,5,1,7,10,12]
#Output: [8,5,10,1,7,null,12]

#Constraints:

#1 <= preorder.length <= 100
#1 <= preorder[i] <= 10^8
#The values of preorder are distinct.

#Solution1 - recursive


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    index = 0
    
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        
        return self.helper(preorder,bound=float('inf'))
            
    def helper(self, A, bound=float('inf')):
        if self.index == len(A) or A[self.index] > bound:
            return None
        root = TreeNode(A[self.index])
        self.index += 1
        root.left = self.helper(A, root.val)
        root.right = self.helper(A, bound)
        return root


#Solution2 - iterative

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