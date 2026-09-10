# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        ans = 0
        def dfs(root):
            nonlocal ans
            if not root:
                return 0, 0
            
            left_sum, left_count = dfs(root.left)
            right_sum, right_count = dfs(root.right)

            total_sum = left_sum + right_sum + root.val
            total_count = left_count + right_count + 1

            if total_sum // total_count == root.val:
                ans += 1
            
            return total_sum, total_count
        
        dfs(root)
        return ans