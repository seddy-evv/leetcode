"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""

from typing import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        lst1 = l1
        lst2 = l2
        node = ListNode(0)
        lst_node = node
        carry = 0
        while lst1 != None or lst2 != None or carry != 0:
            val1 = lst1.val if lst1 != None else 0
            val2 = lst2.val if lst2 != None else 0
            new_node = ListNode((val1 + val2 + carry) % 10)
            lst_node.next = new_node
            carry = (val1 + val2 + carry) // 10
            lst_node = new_node
            lst1 = lst1.next if lst1 != None else None
            lst2 = lst2.next if lst2 != None else None
        return node.next
