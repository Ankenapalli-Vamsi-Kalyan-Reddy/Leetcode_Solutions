# connect_next_right_pointers.py

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

import collections

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        # Initialize queue with root node and its level
        q = collections.deque()
        q.append([root, 0])

        # Perform level-order traversal
        while q:
            pop_num, level = q.popleft()

            # If next node exists and is on the same level, connect `next` pointer
            if q and q[0][1] == level:
                pop_num.next = q[0][0]
            else:
                # Otherwise, this is the last node in the current level
                pop_num.next = None

            # Add left and right children to the queue with incremented level
            if pop_num.left:
                q.append([pop_num.left, level + 1])
            if pop_num.right:
                q.append([pop_num.right, level + 1])

        # Return the modified tree
        return root
