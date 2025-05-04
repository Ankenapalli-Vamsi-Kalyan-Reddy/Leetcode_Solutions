from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque([root])
        average = []
        while queue:
            size = len(queue)
            sum_ = 0
            for _ in range(size):
                ele = queue.popleft()
                sum_ = sum_ + ele.val
                if ele.left is not None:
                    queue.append(ele.left)
                if ele.right is not None:
                    queue.append(ele.right)
            average.append(sum_/size)
        return average
