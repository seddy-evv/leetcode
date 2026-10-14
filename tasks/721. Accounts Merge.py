# Task description:
# Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0]
# is a name, and the rest of the elements are emails representing emails of the account.

# Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some
# common email to both accounts. Note that even if two accounts have the same name, they may belong to different
# people as people could have the same name. A person can have any number of accounts initially, but all of their
# accounts definitely have the same name.

# After merging the accounts, return the accounts in the following format: the first element of each account is the
# name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

# Example 1:

# Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],
# ["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
# Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],
# ["John","johnnybravo@mail.com"]]
# Explanation:
# The first and second John's are the same person as they have the common email "johnsmith@mail.com".
# The third John and Mary are different people as none of their email addresses are used by other accounts.
# We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'],
# ['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.

# Example 2:
# Input: accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
# Output: [["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]

# Constraints:
# 1 <= accounts.length <= 1000
# 2 <= accounts[i].length <= 10
# 1 <= accounts[i][j].length <= 30
# accounts[i][0] consists of English letters.
# accounts[i][j] (for j > 0) is a valid email.


# Union-Find (Disjoint Set Union - DSU) with Path Compression and Rank Optimization
class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def find(self, i: str) -> str:
        # If the email isn't in the map yet, initialize it as its own parent
        if i not in self.parent:
            self.parent[i] = i
            self.rank[i] = 1
            return i

        if self.parent[i] == i:
            return i
        # Path compression optimization
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: str, j: str) -> None:
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i != root_j:
            # Union by rank optimization
            if self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            elif self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            else:
                self.parent[root_j] = root_i
                self.rank[root_i] += 1


class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        uf = UnionFind()
        email_to_name = {}

        # Step 1: Union emails within each account block, and map emails to names
        for account in accounts:
            name = account[0]
            first_email = account[1]

            for email in account[1:]:
                # Link all emails in this group to the first email
                uf.union(first_email, email)
                email_to_name[email] = name

        # Step 2: Group emails together under their respective root representatives
        from collections import defaultdict
        merged_groups = defaultdict(list)

        for email in email_to_name:
            root = uf.find(email)
            merged_groups[root].append(email)

        # Step 3: Format the grouped results with names and sorted emails
        result = []
        for root, emails in merged_groups.items():
            name = email_to_name[root]
            result.append([name] + sorted(emails))

        return result


if __name__ == "__main__":
    sol = Solution()

    # Test case matching LeetCode Example 1
    accounts_input = [
        ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
        ["John", "johnsmith@mail.com", "john00@mail.com"],
        ["Mary", "mary@mail.com"],
        ["John", "johnnybravo@mail.com"]
    ]

    merged_accounts = sol.accountsMerge(accounts_input)
    print("Merged Accounts List:")
    for acc in merged_accounts:
        print(acc)

    # Expected Output:
    # ['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']
    # ['Mary', 'mary@mail.com']
    # ['John', 'johnnybravo@mail.com']


# Time Complexity: O(N*K*log(N*K)), where N is the total number of accounts and K is the maximum number of emails
# in an account. Building the Union-Find structure takes nearly linear time O(A*a(A)) where A is the total number
# of emails. The dominant operation is sorting the emails within each merged component at the final stage, leading
# to a log-linear cost based on the maximum component size.
# Space Complexity: O(N*K) auxiliary space required to maintain the parent, rank, and email_to_name hash maps
# which track every unique email in the dataset.
