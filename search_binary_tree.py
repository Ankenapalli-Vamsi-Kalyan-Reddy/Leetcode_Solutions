# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # This function searches for a node in a binary search tree (BST)
    # with a given value and returns the node if found, otherwise None.
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        # Base case: If the root is None, the value doesn't exist in the tree.
        if root is None:
            return None
        
        # If the current node's value matches the target value, return the node.
        if root.val == val:
            return root
        
        # If the target value is less than the current node's value,
        # search the left subtree (since it's a BST).
        elif root.val >= val:
            return self.searchBST(root.left, val)
        
        # If the target value is greater than the current node's value,
        # search the right subtree.
        else:
            return self.searchBST(root.right, val)
