from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # If the tree is empty, return an empty list
        if root is None:
            return []

        # Initialize queue for BFS with the root node
        queue = deque([root])
        
        # This will store the final level-order traversal result
        family = []

        # Loop until the queue is empty
        while queue:
            # List to store values of nodes at the current level
            inside = []
            # Number of nodes at the current level
            size = len(queue)

            # Process all nodes at this level
            for _ in range(size):
                ele = queue.popleft()  # Get the next node in the queue
                inside.append(ele.val)  # Add its value to the current level

                # Add child nodes to the queue for the next level
                if ele.left is not None:
                    queue.append(ele.left)
                if ele.right is not None:
                    queue.append(ele.right)

            # Add the current level values to the result
            family.append(inside)

        # Return the level-order traversal result
        return family
