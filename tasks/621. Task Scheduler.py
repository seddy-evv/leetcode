# Task description:
# You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n. Each CPU interval can
# be idle or allow the completion of one task. Tasks can be completed in any order, but there's a constraint: there
# has to be a gap of at least n intervals between two tasks with the same label.

# Return the minimum number of CPU intervals required to complete all tasks.

# Example 1:
# Input: tasks = ["A","A","A","B","B","B"], n = 2
# Output: 8
# Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.
# After completing task A, you must wait two intervals before doing A again. The same applies to task B. In the 3rd
# interval, neither A nor B can be done, so you idle. By the 4th interval, you can do A again as 2 intervals
# have passed.
#
# Example 2:
# Input: tasks = ["A","C","A","B","D","B"], n = 1
# Output: 6
# Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.
# With a cooling interval of 1, you can repeat a task after just one other task.

# Example 3:
# Input: tasks = ["A","A","A", "B","B","B"], n = 3
# Output: 10
# Explanation: A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.
# There are only two types of tasks, A and B, which need to be separated by 3 intervals. This leads to idling twice
# between repetitions of these tasks.

# Constraints:
# 1 <= tasks.length <= 104
# tasks[i] is an uppercase English letter.
# 0 <= n <= 100


# Greedy Algorithm via Math Formula Optimization (Max-Frequency Slot Allocation)
from collections import Counter


class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        # Step 1: Count the frequency of each unique task
        task_counts = Counter(tasks)
        frequencies = list(task_counts.values())

        # Step 2: Find the maximum frequency among all tasks
        max_freq = max(frequencies)

        # Step 3: Count how many distinct tasks share this maximum frequency
        max_freq_count = frequencies.count(max_freq)

        # Step 4: Calculate the minimum intervals dictated purely by the skeleton formula
        # Chunks needed = (max_freq - 1)
        # Size of each chunk = (n + 1)
        # Elements left over at the end = max_freq_count
        minimum_intervals = (max_freq - 1) * (n + 1) + max_freq_count

        # Step 5: The answer cannot be smaller than the total number of input tasks.
        # If we have too many distinct tasks, they completely overwrite the idles,
        # making the total time equal to the number of tasks.
        return max(len(tasks), minimum_intervals)


if __name__ == "__main__":
    sol = Solution()

    # Test case matching Example 1
    cpu_tasks = ["A", "A", "A", "B", "B", "B"]
    cooldown = 2

    total_time = sol.leastInterval(cpu_tasks, cooldown)
    print(f"Tasks: {cpu_tasks}, Cooldown n = {cooldown}")
    # Tasks: ['A', 'A', 'A', 'B', 'B', 'B'], Cooldown n = 2
    print(f"Minimum intervals needed: {total_time}")
    # Minimum intervals needed: 8


# Time Complexity: O(N), where N is the total number of tasks in the input array. Scanning the array to generate
# the frequency dictionary maps takes linear O(N) time. Finding the maximum value and matching frequencies
# runs in O(U) time where U is the number of unique task characters. Since U ≤ 26 (bounded by English uppercase letters),
# the math evaluation phase executes in strict constant O(1) time.
# Space Complexity: O(1) constant auxiliary space. The task_counts dictionary can store at most 26 unique 
# tracking keys corresponding to uppercase alphabet characters, keeping extra memory allocations completely 
# independent of the input size growth.
