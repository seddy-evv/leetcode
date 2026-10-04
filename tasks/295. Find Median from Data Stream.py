# Task description:
# The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value,
# and the median is the mean of the two middle values.

# - For example, for arr = [2,3,4], the median is 3.
# - For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.

# Implement the MedianFinder class:
# - MedianFinder() initializes the MedianFinder object.
# - void addNum(int num) adds the integer num from the data stream to the data structure.
# - double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be
# accepted.

# Example 1:
# Input
# ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
# [[], [1], [2], [], [3], []]
# Output
# [null, null, null, 1.5, null, 2.0]

# Explanation
# MedianFinder medianFinder = new MedianFinder();
# medianFinder.addNum(1);    // arr = [1]
# medianFinder.addNum(2);    // arr = [1, 2]
# medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
# medianFinder.addNum(3);    // arr[1, 2, 3]
# medianFinder.findMedian(); // return 2.0

# Constraints:
# -105 <= num <= 105
# There will be at least one element in the data structure before calling findMedian.
# At most 5 * 104 calls will be made to addNum and findMedian.
#
#
# Follow up:
#
# If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
# If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?


# Two Heaps (Max-Heap and Min-Heap Balancing).
import heapq


class MedianFinder:

    def __init__(self):
        """Initializes the data structure."""
        # Max-heap to store the smaller half of the numbers (inverted signs for Python heapq)
        self.small = []
        # Min-heap to store the larger half of the numbers
        self.large = []

    def addNum(self, num: int) -> None:
        """Adds a number from the data stream."""
        # Step 1: Push to max-heap (small). We push negative values to simulate max-heap.
        heapq.heappush(self.small, -num)

        # Step 2: Ensure every element in small is <= every element in large.
        # If the top of small is larger than the top of large, move it over.
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # Step 3: Handle size balance. len(small) can only be up to len(large) + 1
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        """Returns the median of current data stream elements."""
        # If total number of elements is odd, small has the extra median element
        if len(self.small) > len(self.large):
            return float(-self.small[0])

        # If total number of elements is even, find the average of both tops
        return (-self.small[0] + self.large[0]) / 2.0


if __name__ == "__main__":
    median_finder = MedianFinder()

    # Simulate stream insertion matching Example 1
    median_finder.addNum(1)
    median_finder.addNum(2)
    print(f"Median after adding 1 and 2: {median_finder.findMedian()}")  # Output: 1.5

    median_finder.addNum(3)
    print(f"Median after adding 3:       {median_finder.findMedian()}")  # Output: 2.0


# Time Complexity:
# 	• addNum(num): O(log N), where N is the total number of items inserted so far. Pushing and popping from a heap
# 	of size N/2 requires logarithmic time.
# 	• findMedian(): O(1) constant time, as it simply looks up the top element of one or both heaps without running any loops.
# Space Complexity: O(N) auxiliary space required to maintain the distributed data stream across the two heap 
# structures (small and large).
