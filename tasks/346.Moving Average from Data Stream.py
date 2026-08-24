# Task description:
# Moving Average in a Data Stream: Implement a MovingAverage class that takes a stream of numbers and calculates the
# average of the last N elements.

# To achieve O(1) time complexity for calculating the moving average upon receiving each new number, the optimal
# approach utilizes a Queue (specifically collections.deque in Python) to track the sliding window of size N, and an
# integer variable to maintain the running sum of elements inside the window.

# Sliding Window via Queue (First-In, First-Out / FIFO).
from collections import deque

class MovingAverage:
    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.queue = deque()
        self.running_sum = 0.0

    def next(self, val: int) -> float:
        # If the queue has reached max capacity, evict the oldest element
        if len(self.queue) == self.size:
            oldest_val = self.queue.popleft()
            self.running_sum -= oldest_val

        # Add the new value to the queue and update the running sum
        self.queue.append(val)
        self.running_sum += val

        # Calculate and return the average
        return self.running_sum / len(self.queue)


if __name__ == "__main__":
    # Initialize moving average with a window size of 3
    moving_average = MovingAverage(3)

    print(moving_average.next(1))  # Returns 1.0  -> (1 / 1)
    print(moving_average.next(10))  # Returns 5.5  -> ((1 + 10) / 2)
    print(moving_average.next(3))  # Returns 4.67 -> ((1 + 10 + 3) / 3)
    print(moving_average.next(5))  # Returns 6.0  -> ((10 + 3 + 5) / 3) [1 is evicted]

# Complexity Analysis:
# Time Complexity: O(1) per next() invocation. Appending to a deque, popping from the left, and managing arithmetic
# updates take constant time. This completely avoids recalculating the sum from scratch (O(N)) each time.
# Space Complexity: O(N), where N is the maximum window size (size). The queue holds at most N elements at any given
# point in time.


# Key Interview Talking Points
# Preventing Precision Issues: In high-frequency trading or streaming data architectures, keeping a running_sum over
# an infinite sequence of floats can eventually cause floating-point drift (rounding errors). Explain to the interviewer
# that for mission-critical precision, you can maintain integers or reset the exact sum periodically.
# Circular Buffer Alternative: If asked how to optimize this without relying on standard library structures like deque,
# you can mention that an array of size N used as a Circular Buffer with a pointer head = (head + 1) % N yields the same
# complexity while utilizing pre-allocated, contiguous memory.
