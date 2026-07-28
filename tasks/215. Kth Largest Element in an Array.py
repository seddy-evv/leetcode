# Task Description
# Given an integer array nums and an integer k, return the k-th largest element in the array.
# Note: It must be the k-th largest element in sorted order, not the k-th distinct element.
# Example:
# Input: nums = [3, 2, 1, 5, 6, 4], k = 2
# Output: 5 (The sorted array is [1, 2, 3, 4, **5**, 6], and the 2nd largest is 5)


# Theory:
# Step 1: The Brute Force Approach (Sorting)The easiest way is to sort the array in descending order and return
# the element at index k - 1.
# - Time Complexity: (O(NlogN)) due to sorting.
# - Interviewer's reaction: "Good, but can we do better than (O(NlogN)) time?"
# Step 2: The Optimal Approach (Min-Heap)Instead of keeping track of all elements, you only keep track of the k
# largest elements seen so far using a Min-Heap of size k.
# - Iterate through the array and push elements into the Min-Heap.
# - If the size of the heap exceeds k, pop the smallest element out.
# - Because it's a Min-Heap, the smallest numbers are discarded first. By the end of the array, the heap will contain
#   exactly the k largest elements, and the top of the heap (heap[0]) will be the k-th largest.


# Implementation:
import heapq

def findKthLargest(nums: list[int], k: int) -> int:
    # Initialize an empty min-heap
    min_heap = []

    for num in nums:
        # Push the current number onto the heap
        heapq.heappush(min_heap, num)

        # If the heap size exceeds k, remove the smallest element
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    # The root of the min-heap is now the k-th largest element
    return min_heap[0]


# --- Validation ---
print(findKthLargest([3, 2, 1, 5, 6, 4], 2))
# 5

# Complexity Analysis
# Time Complexity: (O(Nlogk))
#  - We iterate through N elements.
#  - Each heap push/pop operation takes (O(log k)) time because the heap size never exceeds k + 1.
#  - Since k ≤ N, this is significantly faster than (O(NlogN)) when k is small.
# Space Complexity: O(k) to store the k elements in the heap.
