# Task Description
# Implement a first-in, first-out (FIFO) queue using only two stacks. The implemented queue should support all the
# functions of a normal queue (push, peek, pop, and empty).Implement the MyQueue class:

# Implement the MyQueue class:
# - push(x): Pushes element x to the back of the queue.
# - pop(): Removes the element from the front of the queue and returns it.
# - peek(): Returns the element at the front of the queue.
# - empty(): Returns true if the queue is empty, false otherwise.

# Notes: You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and
# is empty operations are valid.

class MyQueue:

    def __init__(self):
        self.input_stack = []
        self.output_stack = []

    def push(self, x: int) -> None:
        # Standard stack push
        self.input_stack.append(x)

    def pop(self) -> int:
        # Ensure output_stack has the current oldest elements
        self.peek()
        return self.output_stack.pop()

    def peek(self) -> int:
        # If output_stack is empty, move all elements from input_stack
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())
        return self.output_stack[-1]

    def empty(self) -> bool:
        # The queue is empty only if both stacks are empty
        return not self.input_stack and not self.output_stack


if __name__ == "__main__":
    # Example execution
    queue = MyQueue()
    queue.push(1)
    print(queue.peek())
    # 1
    print(queue.pop())
    # 1
    print(queue.empty())
    # True

# Complexity Analysis
#  Time Complexity:
#  - push: O(1)
#  - pop / peek: Amortized O(1). While moving elements from one stack to another takes O(n) time, each element is
#    moved at most twice (once into input_stack, once into output_stack) across all operations.
#  - empty: O(1)
#  Space Complexity: O(n) – To store a total of n elements in the stacks.
