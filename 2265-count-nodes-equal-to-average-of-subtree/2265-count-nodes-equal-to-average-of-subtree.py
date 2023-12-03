# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        sum_nodes, total_nodes, ans = self.sumofSubtree(root, 0, 0, 0)
        return ans

    # def helper(self, root, ans):
    #     if not root:
    #         return 0
    #     s, n = self.sumofSubtree(root, 0, 0)
    #     if s//n ==root.val:
    #         ans+=1
    #     if root.left:
    #         ans = self.helper(root.left, ans)
    #     if root.right:
    #         ans = self.helper(root.right, ans)
    #     return ans
    def sumofSubtree(self, root, sum_nodes, total_nodes, ans):
        print(ans)
        if not root:
            return sum_nodes, total_nodes, ans
        sum_nodesl, total_nodesl, ans = self.sumofSubtree(root.left, 0, 0, ans)
        sum_nodesr, total_nodesr, ans = self.sumofSubtree(root.right, 0, 0, ans)
        sum_nodes = sum_nodesl+sum_nodesr+root.val
        total_nodes = total_nodesl+total_nodesr+1
        if (sum_nodes//total_nodes)==root.val:
            ans +=1
        return sum_nodes, total_nodes, ans

        