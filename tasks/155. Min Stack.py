# Task description:
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:
# MinStack() initializes the stack object.
# void push(int value) pushes the element value onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.

# Example 1:
# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]
#
# Output
# [null,null,null,null,-3,null,0,-2]
#
# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2

# Constraints:
# -231 <= val <= 231 - 1
# Methods pop, top and getMin operations will always be called on non-empty stacks.
# At most 3 * 104 calls will be made to push, pop, top, and getMin.


# Synchronized Dual Stack Tracking system (or Value-Minimum Coordinate Tracking Pairs)
class MinStack:

    def __init__(self):
        """Initializes the stack object."""
        # Main stack holds the actual numbers
        self.stack = []
        # Min stack keeps track of the running minimum element at each state
        self.min_stack = []

    def push(self, val: int) -> None:
        """Pushes the element val onto the stack."""
        self.stack.append(val)

        # The new minimum is the smaller of the current value or the top of the min_stack
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self) -> None:
        """Removes the element on the top of the stack."""
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()

    def top(self) -> int:
        """Gets the top element of the stack."""
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int:
        """Retrieves the minimum element in the stack."""
        return self.min_stack[-1] if self.min_stack else None


if __name__ == "__main__":
    # Initialize the MinStack instance
    min_stack = MinStack()

    # Simulate the calls from Example 1
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)

    print(f"Current minimum: {min_stack.getMin()}")
    # Current minimum: -3

    min_stack.pop()
    print(f"Top element after pop: {min_stack.top()}")
    # Top element after pop: 0
    print(f"Current minimum after pop: {min_stack.getMin()}")
    # Current minimum after pop: -2


# Time Complexity: O(1) constant runtime for all operations (push, pop, top, and getMin). Dynamic arrays support
# constant-time tail insertions and deletions. The localized minimum tracker avoids scanning components.
# Space Complexity: O(N) auxiliary space, where N is the total number of items pushed onto the stack. The min_stack
# scales linearly alongside the main stack to keep a strict historical log of minimum state boundaries.
