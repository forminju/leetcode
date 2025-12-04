from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        def dfs(node, cur_sum):
            if not node:
                return 0

            cur_sum += node.val

            count = prefix_sums[cur_sum - targetSum]

            prefix_sums[cur_sum] +=1

            count += dfs(node.left, cur_sum)
            count += dfs(node.right, cur_sum)
            prefix_sums[cur_sum] -=1

            return count
        
        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1
        return dfs(root, 0)


        