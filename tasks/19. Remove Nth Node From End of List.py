# Task description:
# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Example 1:
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]

# Example 2:
# Input: head = [1], n = 1
# Output: []

# Example 3:
# Input: head = [1,2], n = 1
# Output: [1]

# Constraints:
# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz

# Follow up: Could you do this in one pass?

# Two-Pointer Technique (Fast and Slow Pointers with a Dummy Node)
from typing import Optional


# Definition for singly-linked list node.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy node pointing to the head
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy

        # Move the fast pointer so there is a gap of n nodes between fast and slow
        for _ in range(n + 1):
            fast = fast.next

        # Move both pointers together until fast reaches the end
        while fast is not None:
            fast = fast.next
            slow = slow.next

        # slow is now right before the node to be removed
        slow.next = slow.next.next

        # Return the actual head of the modified list
        return dummy.next

# Helper function to convert an array into a Linked List
def build_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

# Helper function to print a Linked List
def print_linked_list(head):
    elements = []
    while head:
        elements.append(str(head.val))
        head = head.next
    print(" -> ".join(elements) if elements else "Empty List")

if __name__ == "__main__":
    # Instantiate the solution
    sol = Solution()

    # Example 1: Removing the 2nd node from the end
    list1 = build_linked_list([1, 2, 3, 4, 5])
    result1 = sol.removeNthFromEnd(list1, 2)
    print("Result 1:")
    print_linked_list(result1)
    # Output: 1 -> 2 -> 3 -> 5

    # Example 2: Removing the only node in the list
    list2 = build_linked_list([1])
    result2 = sol.removeNthFromEnd(list2, 1)
    print("\nResult 2:")
    print_linked_list(result2)
    # Output: Empty List


# Time Complexity: O(L), where L is the total number of nodes in the linked list. The algorithm traverses the list
# in a single pass. The fast pointer goes from the dummy node straight to the end of the list, doing exactly L + 1
# node transitions.
# Space Complexity: O(1). The algorithm modifies pointer connections in-place. No extra data structures or copies of
# nodes are created, requiring only constant auxiliary memory.
