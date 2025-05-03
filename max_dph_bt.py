# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0  # Tracks the maximum depth found
        count = 0      # Tracks the current depth during traversal

        def traverse(root):
            nonlocal max_depth, count  # Access and modify outer variables
            if not root:
                # If leaf node is reached, update max_depth if current count is greater
                max_depth = max(max_depth, count)
                return
            count += 1              # Increase depth going down
            traverse(root.left)     # Traverse left subtree
            traverse(root.right)    # Traverse right subtree
            count -= 1              # Decrease depth when backtracking

        traverse(root)  # Start DFS traversal from root
        return max_depth  # Return the maximum depth found
