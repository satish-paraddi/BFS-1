# Time Complexity : O(n)
# Space Complexity : O(n)
# Did this code successfully run on Leetcode : Yes
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque([root])
        if not root:
            return []
        while q:
              size = len(q)
              level = []
              #note that size is locked in
              for _ in range(size):
                 node = q.popleft()
                 level.append(node.val)
                 if node.left:
                    q.append(node.left)
                 if node.right:
                    q.append(node.right)
              res.append(level)
        return res
