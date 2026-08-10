# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.

# Example 1:
# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# text
# 1 -> 4 -> 5,
# 1 -> 3 -> 4,
# 2 -> 6
# Merging them into one sorted list:1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6

# Example 2:
# Input: lists = []
# Output: []

# Example 3:
# Input: lists = [[]]
# Output: []


# Divide and Conquer (Merge Sort Style)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        if not lists:
            return None

        # Continue pairing up and merging until only one list remains
        while len(lists) > 1:
            merged_lists = []

            # Step through the lists in pairs of 2
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                # If there is no second list in the pair (odd length), pass None
                list2 = lists[i + 1] if (i + 1) < len(lists) else None

                # Merge the pair and add it to our tracking array
                merged_lists.append(self.mergeTwoLists(list1, list2))

            lists = merged_lists

        return lists[0]

    def mergeTwoLists(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        """Standard helper function to merge two sorted linked lists (LeetCode 21)."""
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        # Attach the remaining nodes from whichever list isn't empty
        tail.next = l1 if l1 else l2
        return dummy.next


if __name__ == "__main__":
    def create_linked_list(arr):
        if not arr:
            return None
        dummy = ListNode(arr[0])
        curr = dummy
        for val in arr[1:]:
            curr.next = ListNode(val)
            curr = curr.next
        return dummy
    # Constructing the 3 sorted linked lists from Example 1:
    # List 1: 1 -> 4 -> 5
    # List 2: 1 -> 3 -> 4
    # List 3: 2 -> 6
    list1 = create_linked_list([1, 4, 5])
    list2 = create_linked_list([1, 3, 4])
    list3 = create_linked_list([2, 6])
    # The final input parameter array passed to the function
    lists = [list1, list2, list3]
    sol = Solution()
    res = sol.mergeKLists(lists)
    res_lst = []
    while res.next:
        res_lst.append(res.val)
        res = res.next
    print(res_lst)
    # [1, 1, 2, 3, 4, 4, 5]


# Complexity Analysis:
# Time Complexity: O(Nlogk), where N is the total number of nodes across all lists combined, and k
# is the number of linked lists. There are logk total levels of merging, and at each level, we process every
# single node exactly once.
# Space Complexity: O(1) auxiliary space if implemented iteratively. We are only shifting existing
# ListNode pointers in-place without creating entirely new node wrappers or making heavy recursive call stacks
