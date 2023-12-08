# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def tree2str(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        def preorder(node, s):
            if not node:
                return s
            if node:
                s = s+str(node.val)
                s = s+'('
                s = preorder(node.left, s)
                s = s+')'
                s = s+'('
                s = preorder(node.right,s)
                s = s+')'
                if s[-4:] == '()()':
                    s=s[:-4]
                elif s[-2:] =='()':
                    s = s[:-2]
            return s
        s = ''
        return preorder(root, s)
                