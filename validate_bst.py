# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Variables to track nodes for BST violation
        first_node = None
        second_node = None
        prev_node = None
        
        # A single node tree is always a valid BST
        if root.left is None and root.right is None:
            return True
        else:
            # In-order traversal helper function
            def judgebst(rootnode):
                nonlocal prev_node, first_node, second_node
                if not rootnode:
                    return
                # Traverse left subtree
                judgebst(rootnode.left)
                
                # Compare current node value with the previous node value
                if prev_node is not None:
                    if rootnode.val <= prev_node.val:
                        # If BST property is violated, mark nodes
                        if first_node is None:
                            first_node = rootnode
                        second_node = prev_node
                # Update previous node to current node
                prev_node = rootnode

                # Traverse right subtree
                judgebst(rootnode.right)

            # Start in-order traversal
            judgebst(root)

            # If both nodes are set, it's not a valid BST
            if first_node is not None and second_node is not None:
                return False
            else:
                return True
