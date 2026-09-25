# Task description:
# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Example 2:
# Input: head = [1,2]
# Output: [2,1]

# Example 3:
# Input: head = []
# Output: []

# Constraints:

# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000


# Iterative Pointer Reversal (Three-Pointer Traversal)
# 1. ListNode Node Structure Definition
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 2. Iterative Three-Pointer Solution
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head

        while curr:
            next_node = curr.next  # 1. Save the next node reference
            curr.next = prev  # 2. Reverse the current node's pointer
            prev = curr  # 3. Move 'prev' one step forward
            curr = next_node  # 4. Move 'curr' one step forward

        return prev


# --- Helper Utilities for Testing ---

def build_linked_list(elements: list) -> ListNode:
    """Helper to convert a Python list into a sequential Linked List."""
    if not elements:
        return None

    head = ListNode(elements[0])
    current = head
    for value in elements[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


def print_linked_list(head: ListNode) -> list:
    """Helper to traverse a linked list and output values as a list."""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


# --- Execution Simulation ---
if __name__ == "__main__":
    # Test Case matching Example 1: 1 -> 2 -> 3 -> 4 -> 5
    input_array = [1, 2, 3, 4, 5]
    linked_list_head = build_linked_list(input_array)

    print(f"Original list: {print_linked_list(linked_list_head)}")

    # Run the Reversal Engine
    sol = Solution()
    reversed_head = sol.reverseList(linked_list_head)

    print(f"Reversed list: {print_linked_list(reversed_head)}")
    # Expected Output: [5, 4, 3, 2, 1]


# Time Complexity: O(N), where N is the number of nodes in the linked list. The algorithm traverses the list linearly
# exactly once.
# Space Complexity: O(1) auxiliary space. The reversal is done entirely in-place by changing node pointer directions,
# requiring no additional data structures.
