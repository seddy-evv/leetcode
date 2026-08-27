# Task description:
# On an infinite plane, a robot initially stands at (0, 0) and faces north. Note that:
# - The north direction is the positive direction of the y-axis.
# - The south direction is the negative direction of the y-axis.
# - The east direction is the positive direction of the x-axis.
# - The west direction is the negative direction of the x-axis.

# The robot can receive one of three instructions:
# - "G": go straight 1 unit.
# - "L": turn 90 degrees to the left (i.e., anti-clockwise direction).
# - "R": turn 90 degrees to the right (i.e., clockwise direction).
# The robot performs the instructions given in order, and repeats them forever.
# Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.

# Example 1:
# Input: instructions = "GGLLGG"
# Output: true
# Explanation: The robot is initially at (0, 0) facing the north direction.
# "G": move one step. Position: (0, 1). Direction: North.
# "G": move one step. Position: (0, 2). Direction: North.
# "L": turn 90 degrees anti-clockwise. Position: (0, 2). Direction: West.
# "L": turn 90 degrees anti-clockwise. Position: (0, 2). Direction: South.
# "G": move one step. Position: (0, 1). Direction: South.
# "G": move one step. Position: (0, 0). Direction: South.
# Repeating the instructions, the robot goes into the cycle: (0, 0) --> (0, 1) --> (0, 2) --> (0, 1) --> (0, 0).
# Based on that, we return true.

# Example 2:
# Input: instructions = "GG"
# Output: false
# Explanation: The robot is initially at (0, 0) facing the north direction.
# "G": move one step. Position: (0, 1). Direction: North.
# "G": move one step. Position: (0, 2). Direction: North.
# Repeating the instructions, keeps advancing in the north direction and does not go into cycles.
# Based on that, we return false.

# Example 3:
# Input: instructions = "GL"
# Output: true
# Explanation: The robot is initially at (0, 0) facing the north direction.
# "G": move one step. Position: (0, 1). Direction: North.
# "L": turn 90 degrees anti-clockwise. Position: (0, 1). Direction: West.
# "G": move one step. Position: (-1, 1). Direction: West.
# "L": turn 90 degrees anti-clockwise. Position: (-1, 1). Direction: South.
# "G": move one step. Position: (-1, 0). Direction: South.
# "L": turn 90 degrees anti-clockwise. Position: (-1, 0). Direction: East.
# "G": move one step. Position: (0, 0). Direction: East.
# "L": turn 90 degrees anti-clockwise. Position: (0, 0). Direction: North.
# Repeating the instructions, the robot goes into the cycle: (0, 0) --> (0, 1) --> (-1, 1) --> (-1, 0) --> (0, 0).
# Based on that, we return true.

# Constraints:
# 1 <= instructions.length <= 100
# instructions[i] is 'G', 'L' or, 'R'.


# Vector-Based Vectorial Simulation with Directional State Analysis
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # Initial position coordinates
        x, y = 0, 0

        # Direction vectors mapping to directions: 0 = North, 1 = East, 2 = South, 3 = West
        # Moving North increases y, East increases x, South decreases y, West decreases x
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # Start facing North (index 0)
        current_dir = 0

        # Execute the instruction string exactly once
        for move in instructions:
            if move == 'R':
                # Turn clockwise
                current_dir = (current_dir + 1) % 4
            elif move == 'L':
                # Turn counter-clockwise
                current_dir = (current_dir - 1) % 4
            elif move == 'G':
                # Advance forward based on current active vector
                dx, dy = directions[current_dir]
                x += dx
                y += dy

        # Condition for a loop:
        # 1. Back at the origin (x == 0 and y == 0)
        # 2. Facing ANY direction other than North (current_dir != 0)
        return (x == 0 and y == 0) or (current_dir != 0)


# --- Example Usage ---
if __name__ == "__main__":
    sol = Solution()
    print(sol.isRobotBounded("GL"))
    # Output: True


# Complexity Analysis:
# Time Complexity: O(N), where N is the length of the string instructions. The simulation runs through the instruction
# set exactly once.
# Space Complexity: O(1) auxiliary space. The program updates fixed primitive integer variables (x, y, current_dir)
# using a constant number of tracking direction arrays.
