# Task description:
# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

# Example 1:
# Input: head = [1,2,3,4]
# Output: [1,4,2,3]

# Example 2:
# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]

# Constraints:

# The number of nodes in the list is in the range [1, 5 * 104].
# 1 <= Node.val <= 1000

# Three-Stage Linked List Manipulation (Find Midpoint → Reverse Second Half → Interleave/Merge)
from typing import Optional


# Definition for singly-linked list node.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        # Step 1: Find the middle of the linked list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half of the list
        # slow.next is the start of the second half
        prev, curr = None, slow.next
        slow.next = None  # Disconnect the first half from the second half

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # 'prev' now points to the head of the reversed second half

        # Step 3: Interleave/Merge the two halves
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2

# Helper function to convert a Python list into a Linked List
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

    # Example 1: Odd number of elements
    list1 = build_linked_list([1, 2, 3, 4, 5])
    sol.reorderList(list1)
    print("Result 1:")
    print_linked_list(list1)
    # Output: 1 -> 5 -> 2 -> 4 -> 3

    # Example 2: Even number of elements
    list2 = build_linked_list([1, 2, 3, 4])
    sol.reorderList(list2)
    print("\nResult 2:")
    print_linked_list(list2)
    # Output: 1 -> 4 -> 2 -> 3

# Time Complexity: O(N), where N is the number of nodes in the linked list.
# - Finding the middle takes O(N/2) steps.
# - Reversing the second half takes O(N/2) steps.
# - Interleaving the lists takes O(N/2) steps.
# - Combining these operations results in an overall linear time complexity.
# Space Complexity: O(1). The algorithm restructures pointer nodes entirely in-place. No extra arrays, lists, or
# recursive execution call stacks are utilized, preserving strict constant memory usage.
