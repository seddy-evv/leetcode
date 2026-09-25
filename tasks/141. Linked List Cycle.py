# Task description:
# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously
# following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.

# Example 1:
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

# Example 2:
# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

# Example 3:
# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.

# Constraints:
# The number of the nodes in the list is in the range [0, 104].
# -105 <= Node.val <= 105
# pos is -1 or a valid index in the linked-list.


# Follow up: Can you solve it using O(1) (i.e. constant) memory?

# Floyd's Cycle-Finding Algorithm (commonly known as the Tortoise and the Hare Algorithm or Two-Pointer Cycle Detection).
# 1. ListNode Node Structure Definition
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 2. Floyd's Tortoise and Hare Cycle Detection Solution
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next  # Moves 1 step
            fast = fast.next.next  # Moves 2 steps

            # If they intersect, a circular cycle loop exists
            if slow == fast:
                return True

        return False


# --- Helper Utilities for Testing ---

def create_linked_list_with_cycle(elements: list, pos: int) -> ListNode:
    """
    Helper to convert a Python list into a Linked List.
    If pos >= 0, it loops the tail back to the node at index 'pos'.
    """
    if not elements:
        return None

    head = ListNode(elements[0])
    current = head
    cycle_start_node = None

    if pos == 0:
        cycle_start_node = head

    # Build the linear sequence
    for i in range(1, len(elements)):
        current.next = ListNode(elements[i])
        current = current.next
        if i == pos:
            cycle_start_node = current

    # Connect the tail pointer back to create the cycle loop
    if pos != -1 and cycle_start_node is not None:
        current.next = cycle_start_node

    return head


# --- Execution Simulation ---

if __name__ == "__main__":
    sol = Solution()

    # Test Case 1 matching Example 1: 3 -> 2 -> 0 -> -4 -> (loops back to 2)
    # The node value 2 is at index 1, so pos = 1
    input_elements_1 = [3, 2, 0, -4]
    pos_1 = 1
    cycled_list_head = create_linked_list_with_cycle(input_elements_1, pos_1)

    print(f"Case 1 (Cycled List, pos={pos_1}) Result: {sol.hasCycle(cycled_list_head)}")
    # Expected Output: True

    # Test Case 2 matching Example 3: 1 -> None (No cycle)
    input_elements_2 = [1]
    pos_2 = -1
    linear_list_head = create_linked_list_with_cycle(input_elements_2, pos_2)

    print(f"Case 2 (Linear List, pos={pos_2}) Result: {sol.hasCycle(linear_list_head)}")
    # Expected Output: False


# Time Complexity: O(N), where N is the total number of nodes in the linked list. If no cycle exists, the fast pointer
# reaches the end in O(N) steps. If a cycle exists, the fast pointer enters the loop and catches up to the slow
# pointer within a bounded number of iterations proportional to the loop size.
# Space Complexity: O(1) auxiliary space. Only two pointer trackers (slow and fast) are maintained in memory,
# requiring no additional hashing sets or arrays.
