# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        min_value = float("inf")  # Initialize minimum difference to infinity
        current_value = None      # To store the value of the previously visited node
        current_diff = 0          # Current difference between consecutive nodes

        def findmindiff(rootnode):
            nonlocal min_value, current_value, current_diff  # Allow modification of variables outside nested function
            if not rootnode:
                return
            # Traverse left subtree
            findmindiff(rootnode.left)

            # Process current node
            if current_value is not None:
                current_diff = rootnode.val - current_value
                min_value = min(min_value, current_diff)  # Update min_value if current_diff is smaller
            current_value = rootnode.val  # Update current_value to the current node's value

            # Traverse right subtree
            findmindiff(rootnode.right)

        findmindiff(root)  # Start in-order traversal
        return min_value   # Return the minimum difference found
