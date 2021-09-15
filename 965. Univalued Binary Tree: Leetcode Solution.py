# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isUnivalTree(self,root):
        self.start = root.val
        self.status = True
        def inner(root):
            if not root:
                return True
            left,right = inner(root.left),inner(root.right)
            if root.val != self.start:
                self.status = False

        inner(root)
        return self.status

