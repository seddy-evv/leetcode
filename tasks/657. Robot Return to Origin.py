# Task description:
# There is a robot starting at the position (0, 0), the origin, on a 2D plane. Given a sequence of its moves, judge if
# this robot ends up at (0, 0) after it completes its moves.
# You are given a string moves that represents the move sequence of the robot where moves[i] represents its ith move.
# Valid moves are 'R' (right), 'L' (left), 'U' (up), and 'D' (down).
# Return true if the robot returns to the origin after it finishes all of its moves, or false otherwise.
# Note: The way that the robot is "facing" is irrelevant. 'R' will always make the robot move to the right once,
# 'L' will always make it move left, etc. Also, assume that the magnitude of the robot's movement is the same for each move.

# Example 1:
# Input: moves = "UD"
# Output: true
# Explanation: The robot moves up once, and then down once. All moves have the same magnitude, so it ended up at
# the origin where it started. Therefore, we return true.

# Example 2:
# Input: moves = "LL"
# Output: false
# Explanation: The robot moves left twice. It ends up two "moves" to the left of the origin. We return false because
# it is not at the origin at the end of its moves.

# Constraints:
# 1 <= moves.length <= 2 * 104
# moves only contains the characters 'U', 'D', 'L' and 'R'.


# Coordinate Simulation via Frequency Counting.
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # A robot returns to (0,0) if total Lefts equal Rights
        # and total Ups equal Downs.
        return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')

# --- Alternative Axis-Simulation Approach ---
# class Solution:
#     def judgeCircle(self, moves: str) -> bool:
#         x, y = 0, 0
#         for move in moves:
#             if move == 'U': y += 1
#             elif move == 'D': y -= 1
#             elif move == 'R': x += 1
#             elif move == 'L': x -= 1
#         return x == 0 and y == 0


# --- Example Usage ---
if __name__ == "__main__":
    sol = Solution()
    moves = "UD"
    print(sol.judgeCircle(moves))
    # True


# Complexity Analysis:
# Time Complexity: O(N), where N is the total length of the moves string. The .count() built-in method
# scans the entire sequence of instructions in linear time.
# Space Complexity: O(1) auxiliary space, because we are counting specific properties directly inline without
# instantiating any growth-bound collections or data structures.
