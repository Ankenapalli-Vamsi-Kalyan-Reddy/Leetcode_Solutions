# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # Using DFS to traverse only necessary parts of the tree
        # Skips entire subtrees that are out of range, making it more efficient
        count = 0
        def okit(node, low, high):
            nonlocal count
            if not node:
                return 
            # Add node's value if it's within the given range
            if low <= node.val <= high:
                count = count + node.val
            
            # Only explore left subtree if there's a chance of finding valid values
            if low < node.val:
                okit(node.left, low, high)
            # Only explore right subtree if there's a chance of finding valid values
            if node.val < high:
                okit(node.right, low, high)
        
        okit(root, low, high)
        return count
