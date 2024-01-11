# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans = [0]
        def get_min_max_kids(node, min_val, max_val):
            if not node:
                return
            if (min_val == -1):
                min_val = node.val
                max_val = node.val
            else:
                ans[0] = max(abs(node.val-min_val), abs(node.val - max_val), ans[0])
            min_val = min(node.val, min_val)
            max_val = max(node.val, max_val)
            get_min_max_kids(node.left, min_val, max_val)
            get_min_max_kids(node.right, min_val, max_val)
            
        get_min_max_kids(root, -1, -1)    
        return ans[0]
                
                
        