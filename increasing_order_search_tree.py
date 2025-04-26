# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Helper function to perform in-order traversal
        def in_order(nodes):
            nonlocal current
            if not nodes:
                return
            # Traverse the left subtree first
            in_order(nodes.left)
            # Set the left child to None
            nodes.left = None
            # Connect the current node's right to the visited node
            current.right = nodes
            # Move current to the newly added node
            current = current.right
            # Traverse the right subtree
            in_order(nodes.right)
        
        # Create a dummy node to act as the previous node to the first element
        dummy_node = TreeNode(-1)
        current = dummy_node
        # Start in-order traversal from root
        in_order(root)
        # Return the right child of dummy node which is the new root
        return dummy_node.right
