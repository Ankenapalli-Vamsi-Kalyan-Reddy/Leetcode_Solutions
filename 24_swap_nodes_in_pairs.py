# 24_swap_nodes_in_pairs.py

# Definition for singly-linked list.
# This class represents a node in a singly linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val  # Value of the node
        self.next = next  # Pointer to the next node

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: If the list is empty or has only one node, return it as-is.
        if head is None or head.next is None:
            return head
        
        # Identify the second node, which will become the new head of this swapped pair.
        temp = head.next

        # Recursively swap the rest of the list starting from the third node.
        head.next = self.swapPairs(head.next.next)

        # Point the second node to the first to complete the swap.
        temp.next = head

        # Return the new head node after swapping.
        return temp
