# Task description:
# Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously
# following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is
# connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.
# Do not modify the linked list.

# Example 1:
# Input: head = [3,2,0,-4], pos = 1
# Output: tail connects to node index 1
# Explanation: There is a cycle in the linked list, where tail connects to the second node.

# Example 2:
# Input: head = [1,2], pos = 0
# Output: tail connects to node index 0
# Explanation: There is a cycle in the linked list, where tail connects to the first node.

# Example 3:
# Input: head = [1], pos = -1
# Output: no cycle
# Explanation: There is no cycle in the linked list.

# Constraints:
# The number of the nodes in the list is in the range [0, 10^4].
# -10^5 <= Node.val <= 10^5
# pos is -1 or a valid index in the linked-list.


# Floyd's Tortoise and Hare Algorithm (also known as Cycle Detection with Phase 2 Intersection Alignment)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None

        tortoise = head
        hare = head

        # Phase 1: Determine if a structural cycle loop exists
        while hare and hare.next:
            tortoise = tortoise.next
            hare = hare.next.next

            # If they meet, a cycle exists
            if tortoise == hare:
                # Phase 2: Find the starting point of the loop
                # Reset tortoise to the head of the linked list
                tortoise = head

                # Move both pointers forward at an equal speed of 1 step
                while tortoise != hare:
                    tortoise = tortoise.next
                    hare = hare.next

                # The point where they meet again is the exact start of the loop
                return tortoise

        return None


if __name__ == "__main__":
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)
    node5 = ListNode(5)
    node6 = ListNode(6)
    node7 = ListNode(7)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    node7.next = node2

    sol = Solution()
    print(sol.detectCycle(node1).val)
    # 2


# Complexity Analysis:
# Time Complexity: O(N), where N is the total number of nodes in the linked list. In Phase 1, the fast pointer loops
# through the cycle space quickly. In Phase 2, the pointers travel a linear distance strictly bounded by the size of
# the list.
# Space Complexity: O(1) auxiliary space. We only use two pointer trackers (tortoise and hare) without keeping any
# history maps or sets.

