# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Recovers a binary search tree where two nodes are swapped by mistake.
        This function corrects the tree in-place using in-order traversal.
        """
        # Pointers to track previous node, and the two nodes to be swapped
        prev = None
        first = None
        second = None

        # Helper function for in-order traversal to detect swapped nodes
        def find(rootnode):
            nonlocal prev, first, second
            if not rootnode:
                return

            # Traverse left subtree
            find(rootnode.left)

            # Detect misplaced nodes in the in-order sequence
            if prev is not None and prev.val > rootnode.val:
                # First wrong node found
                if first is None:
                    first = prev
                # Second wrong node (might update multiple times)
                second = rootnode

            # Update previous node
            prev = rootnode

            # Traverse right subtree
            find(rootnode.right)

        # Start in-order traversal from root
        find(root)

        # Swap the values of the two incorrect nodes to fix the BST
        if first and second:
            first.val, second.val = second.val, first.val
