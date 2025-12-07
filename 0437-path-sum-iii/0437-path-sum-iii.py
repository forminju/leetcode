# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix_sum_count = {0:1} # 해시맵으로 구현. 누적합이 0인 경로 1개로 시작.

        def dfs(node, cur_sum):
            if not node:
                return 0

            cur_sum += node.val # 현재까지 누적합

            count = prefix_sum_count.get(cur_sum - targetSum, 0)
            prefix_sum_count[cur_sum] = prefix_sum_count.get(cur_sum, 0) + 1

            count += dfs(node.left, cur_sum)
            count += dfs(node.right, cur_sum)

            prefix_sum_count[cur_sum] -=1 # 백트래킹. 경로 탐색 끝났으니.

            return count

        return dfs(root, 0)
        