# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # Initialize low and high pointers for the array
        low = 0
        high = len(nums) - 1
        
        # Helper function to recursively construct the BST
        def constructBST(nums, low, high):
            # Base case: when the low index exceeds high, return None (no node to create)
            if low > high:
                return None
            
            # Find the middle element to use as the root of the current subtree
            mid = (low + high) // 2
            
            # Create the current node with the middle element value
            new_node = TreeNode(nums[mid])
            
            # Recursively build the left subtree
            new_node.left = constructBST(nums, low, mid - 1)
            
            # Recursively build the right subtree
            new_node.right = constructBST(nums, mid + 1, high)
            
            # Return the current node
            return new_node
        
        # Start the BST construction from the entire array
        return constructBST(nums, low, high)
