from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        ans = []
        q = deque()

        q.append((root, 0))

        while q:
            node, level = q.popleft()

            if level < len(ans):
                ans[level] = node.val

            else:
                ans.append(node.val)

            if node.left:
                q.append((node.left, level+1))

            if node.right:
                q.append((node.right, level+1))

        return ans
        
        