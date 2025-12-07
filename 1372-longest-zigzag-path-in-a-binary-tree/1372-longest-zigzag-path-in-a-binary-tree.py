# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 각 노드 한 번 씩 방문 => 왼쪽으로 시작하는 지그재그 / 오른쪽으로 시작하는 지그재그
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def dfs(node):
            if not node:
                return -1, -1

            left_l, left_r = dfs(node.left)
            right_l, right_r = dfs(node.right)

            go_left = left_r + 1
            go_right = right_l + 1

            self.ans = max(self.ans , go_left, go_right)

            return go_left, go_right

        dfs(root)
        return self.ans