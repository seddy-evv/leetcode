# There are n cars at given miles away from the starting mile 0, traveling to reach the mile target.
# You are given two integer arrays position and speed, both of length n, where position[i] is the starting mile of the
# ith car and speed[i] is the speed of the ith car in miles per hour.
# A car cannot pass another car, but it can catch up and then travel next to it at the speed of the slower car.
# A car fleet is a single car or a group of cars driving next to each other. The speed of the car fleet is the minimum
# speed of any car in the fleet.
# If a car catches up to a car fleet at the mile target, it will still be considered as part of the car fleet.
# Return the number of car fleets that will arrive at the destination.

# Example 1:
# Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
# Output: 3
# Explanation:
# - The cars starting at 10 (speed 2) and 8 (speed 4) become a fleet, meeting each other at 12. The fleet forms at target.
# - The car starting at 0 (speed 1) does not catch up to any other car, so it is a fleet by itself.
# - The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet, meeting each other at 6. The fleet moves at speed 1
#   until it reaches target.

# Example 2:
# Input: target = 10, position = [3], speed = [3]
# Output: 1
# Explanation:
# There is only one car, hence there is only one fleet.

# Example 3:
# Input: target = 100, position = [0,2,4], speed = [4,2,1]
# Output: 1
# Explanation:
# - The cars starting at 0 (speed 4) and 2 (speed 2) become a fleet, meeting each other at 4. The car starting at 4
# (speed 1) travels to 5.
# - Then, the fleet at 4 (speed 2) and the car at position 5 (speed 1) become one fleet, meeting each other at 6. The
# fleet moves at speed 1 until it reaches target.

# Constraints:
# n == position.length == speed.length
# 1 <= n <= 105
# 0 < target <= 106
# 0 <= position[i] < target
# All the values of position are unique.
# 0 < speed[i] <= 106


# Monotonic Decreasing Stack with Reverse Sorting
class Solution:

    def carFleet(
        self, target: int, position: list[int], speed: list[int]
    ) -> int:
        # Pair position and speed together, then sort by position descending.
        # This allows us to process cars from right to left (closest to target first).
        cars = sorted(zip(position, speed), reverse=True)

        # Stack to hold the arrival times of the leading cars of each fleet.
        fleet_times = []

        for pos, spd in cars:
            # Calculate the time needed for the current car to reach the target solo.
            time_to_target = (target - pos) / spd

            # If the stack is empty, this is the first car closest to the target.
            # If time_to_target is STRICTLY GREATER than the fleet ahead (fleet_times[-1]),
            # it cannot catch up and forms a brand-new, slower car fleet behind.
            if not fleet_times or time_to_target > fleet_times[-1]:
                fleet_times.append(time_to_target)

            # Note: If time_to_target <= fleet_times[-1], it catches up to the fleet ahead.
            # Since it cannot pass, it merges into that fleet and gets bottlenecked,
            # so we safely ignore it (do not push its time onto the stack).

        # The total number of unique fleets corresponds to the size of the stack.
        return len(fleet_times)


if __name__ == "__main__":
    target = 12
    position = [10, 8, 0, 5, 3]
    speed = [2, 4, 1, 1, 3]
    sol = Solution()
    res = sol.carFleet(target, position, speed)
    print(res)
    # 3

# Complexity Analysis:
# Time Complexity: O(nlogn), where n is the number of cars. Pairing the values and sorting them
# by their initial starting positions takes O(nlogn) time. The subsequent linear sweep through the
# array takes single O(n) time.
# Space Complexity: O(n) auxiliary space to hold the sorted unset cars  list structure and the active
# unset fleet_times  monotonic stack contents.
