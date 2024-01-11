# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        
        def get_kids(node, ans):
            if not node:
                return ans
            ans.append(node.val)
            get_kids(node.left,ans)
            get_kids(node.right,ans)
            return ans
        
        def get_ans(ans, node):
            if not node:
                return ans
            kids = get_kids(node, [])
            for k in kids:
                ans = max(ans, abs(node.val- k))
            ans = get_ans(ans, node.left)
            ans = get_ans(ans, node.right)
            return ans
        return get_ans(0, root)
                
                
        