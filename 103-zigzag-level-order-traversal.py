# 103. Binary Tree Zigzag Level Order Traversal
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        # Initialize a queue for level-order traversal
        q = collections.deque()
        q.append(root)

        # Flag to control the zigzag direction
        trig = True

        # Final result list
        list_ = []

        # Process the tree level by level
        while q:
            sublist = []

            # Iterate over all nodes at the current level
            for i in range(len(q)):
                popped = q.popleft()

                # Always add children left to right into the queue
                if trig == True or trig == False:
                    if popped.left:
                        q.append(popped.left)
                    if popped.right:
                        q.append(popped.right)

                # Append current node value
                sublist.append(popped.val)

            # If the current direction is right to left, reverse the sublist
            if trig == False:
                sublist = sublist[::-1]

            # Add the current level's values to the final result
            list_.append(sublist)

            # Toggle direction for next level
            trig = not(trig)

        return list_
