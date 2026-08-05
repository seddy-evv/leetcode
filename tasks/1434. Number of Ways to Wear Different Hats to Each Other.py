# There are n people and 40 types of hats labeled from 1 to 40. Given a 2D integer array hats, where hats[i] is a
# list of all hats preferred by the i-th person, return the number of ways that n people can wear different hats
# from each other. Since the answer may be too large, return it modulo 10^9 + 7.

# Constraints:
# n == hats.length (where <= n <= 10)
# 1 <= hats[i].length <= 40
# 1 <= hats[i][j] <= 40


# Dynamic Programming with Bitmasking (Bitmask DP)
from collections import defaultdict


class Solution:
    def numberWays(self, hats: list[list[int]]) -> int:
        MOD = 10 ** 9 + 7
        n = len(hats)

        # Map each hat to the list of people who prefer it
        # This allows fast lookups when processing hat by hat
        hat_to_people = defaultdict(list)
        for person_id, preferred_hats in enumerate(hats):
            for hat in preferred_hats:
                hat_to_people[hat].append(person_id)

        # Target mask when all people have a hat (e.g., for n=3, 111 in binary is 7)
        all_assigned_mask = (1 << n) - 1

        # Memoization table: dp(hat_id, current_mask)
        memo = {}

        def dp(hat, mask):
            # Base Case 1: All people have received a hat successfully
            if mask == all_assigned_mask:
                return 1
            # Base Case 2: Out of hats, but not all people have been assigned one
            if hat > 40:
                return 0

            # Return cached result if already calculated
            if (hat, mask) in memo:
                return memo[(hat, mask)]

            # Option 1: Do not assign the current hat to anyone
            ways = dp(hat + 1, mask)

            # Option 2: Assign the current hat to an available person who likes it
            for person in hat_to_people[hat]:
                # Check if the person does NOT have a hat yet using bitwise AND
                if not (mask & (1 << person)):
                    # Bitwise OR sets the person's bit to 1 (marking them as assigned)
                    ways += dp(hat + 1, mask | (1 << person))
                    ways %= MOD

            memo[(hat, mask)] = ways
            return ways

        # Start processing from Hat 1 with an empty bitmask (0)
        return dp(1, 0)


if __name__ == "__main__":
    hats = [[3, 5, 1], [3, 5]]
    sol = Solution()
    print(sol.numberWays(hats))
    # 4

    # Way 1: Person 0 wears Hat 3, Person 1 wears Hat 5.
    # Way 2: Person 0 wears Hat 5, Person 1 wears Hat 3.
    # Way 3: Person 0 wears Hat 1, Person 1 wears Hat 3.
    # Way 4: Person 0 wears Hat 1, Person 1 wears Hat 5.


# Time Complexity: O(40*2^n*n)). There are O(40*2^n) unique states in our DP matrix. For each state, we iterate \
# through the people who like the current hat (at most n) people). Given n<=10, 40*1024*10 = 10^5 operations, which
# easily executes within milliseconds.
# Space Complexity: O(40*2^n) to store the memoization cache states.
