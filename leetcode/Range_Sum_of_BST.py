# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        #using DFS
        def dfs(node):
            sum_=0

            #if node is None -> return 0
            if not node:
                return 0

            #sum_ : values of nodes with a value in the range [low, high]
            if node.val>=low and node.val<=high:
                sum_+=node.val
            
            sum_+=dfs(node.left)
            sum_+=dfs(node.right)
            
            return sum_
        
        return dfs(root)
