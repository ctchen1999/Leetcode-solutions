# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque([root])
        ans = []
        while queue:
            queueLength = len(queue)
            levelSum = 0
            for i in range(queueLength):
                node = queue.popleft()
                levelSum += node.val
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            ans.append(levelSum / queueLength)
        return ans