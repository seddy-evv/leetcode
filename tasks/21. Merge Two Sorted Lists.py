# Task description:
# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

# Example 1:
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Example 2:
# Input: list1 = [], list2 = []
# Output: []

# Example 3:
# Input: list1 = [], list2 = [0]
# Output: [0]

# Constraints:
#
# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.

# Two-Pointer Linear Scan (Iterative Simulation with a Dummy Node)
from typing import Optional


# Definition for singly-linked list node.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to act as the root of the merged list
        dummy = ListNode(-1)
        current = dummy

        # Traverse both lists until one of them is exhausted
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next  # Move the tracking pointer forward

        # Append the remaining nodes from whichever list is not empty
        current.next = list1 if list1 else list2

        # Return the actual head of the merged list (skipping the dummy node)
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

# Instantiate the solution
sol = Solution()

# Example 1: Standard lists merge
l1 = build_linked_list([1, 2, 4])
l2 = build_linked_list([1, 3, 4])
merged = sol.mergeTwoLists(l1, l2)
print("Result 1:")
print_linked_list(merged)
# Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4

# Example 2: Merging with an empty list
l3 = build_linked_list([])
l4 = build_linked_list([0])
merged_empty = sol.mergeTwoLists(l3, l4)
print("\nResult 2:")
print_linked_list(merged_empty)
# Output: 0


# Time Complexity: O(N + M), where N and M are the number of nodes in list1 and list2 respectively. In the worst-case
# scenario, the while loop runs until we examine nearly all elements of both lists, comparing values exactly once per
# loop iteration.
# Space Complexity: O(1). The algorithm merges the lists in-place by altering the pointer references (.next) of the
# existing nodes. No extra node allocations are performed except for the single initialization of the temporary dummy node.
