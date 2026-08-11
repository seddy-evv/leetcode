# Given arrival and departure times of all trains that reach a railway station, find the minimum number of platforms
# required for the railway station so that no train is kept waiting.
# arrival = [9:00, 9:40, 9:50, 11:00, 15:00, 18:00]
# departure = [9:10, 12:00, 11:20, 11:30, 19:00, 20:00]

# Example 1:
# Input: arrival = [900, 940, 950, 1100, 1500, 1800], departure = [910, 1200, 1120, 1130, 1900, 2000]
# Output: 3
# Explanation:
# Between 9:40 and 11:20, there are 3 trains at the station simultaneously (the ones that arrived at 9:40, 9:50,
# and 11:00). Hence, a minimum of 3 platforms are needed.


# Greedy Algorithm with Sorting (Two-Pointer Chronological Sweep)
class Solution:
    def findPlatform(self, arrival: list[int], departure: list[int]) -> int:
        # Sort both arrival and departure times independently
        arrival.sort()
        departure.sort()

        # Pointers to track the current arrival and departure events
        arr_ptr = 0
        dep_ptr = 0

        current_platforms = 0
        max_platforms = 0
        n = len(arrival)

        # Chronological sweep through the timeline
        while arr_ptr < n and dep_ptr < n:
            # If the next event is a train arriving
            if arrival[arr_ptr] <= departure[dep_ptr]:
                current_platforms += 1
                arr_ptr += 1

                # Update global peak platforms required
                max_platforms = max(max_platforms, current_platforms)
            else:
                # The next event is a train leaving, freeing up a platform
                current_platforms -= 1
                dep_ptr += 1

        return max_platforms


if __name__ == "__main__":
    # arrival = [9:00, 9: 40, 9: 50, 11: 00, 15: 00, 18: 00]
    # departure = [9:10, 12: 00, 11: 20, 11: 30, 19: 00, 20: 00]
    arrival = [900, 940, 950, 1100, 1500, 1800]
    departure = [910, 1200, 1120, 1130, 1900, 2000]
    sol = Solution()
    res = sol.findPlatform(arrival, departure)
    print(res)
    # 3


# Complexity Analysis:
# Time Complexity: O(NlogN), where N is the number of trains. Sorting the arrival and departure arrays
# takes O(NlogN) time, while the subsequent two-pointer chronological sweep runs in linear O(N) time.
# Space Complexity: O(1) auxiliary space if the input arrays are allowed to be sorted in-place, making it highly
# memory efficient.
