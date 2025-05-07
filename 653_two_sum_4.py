# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # A set to store values we have seen so far
        store_values = set()
        
        # Flag to indicate if a valid pair is found
        validate = False

        # Helper function to perform in-order traversal and search for the complement
        def search(root, k):
            nonlocal store_values, validate
            if not root:
                return

            # Traverse the left subtree
            search(root.left, k)

            # Check if the complement (k - current value) exists in the set
            if (k - root.val) in store_values:
                validate = True
                return

            # Add current value to the set
            store_values.add(root.val)

            # Traverse the right subtree
            search(root.right, k)

        # Start the recursive search
        search(root, k)
        return validate
