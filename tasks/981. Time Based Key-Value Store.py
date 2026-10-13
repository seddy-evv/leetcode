# Task description:
# Design a time-based key-value data structure that can store multiple values for the same key at different time stamps
# and retrieve the key's value at a certain timestamp.
#
# Implement the TimeMap class:
#
# TimeMap() Initializes the object of the data structure.
# void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
# String get(String key, int timestamp) Returns a value such that set was called previously,
# with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with
# the largest timestamp_prev. If there are no values, it returns "".

# Example 1:
# Input
# ["TimeMap", "set", "get", "get", "set", "get", "get"]
# [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
# Output
# [null, null, "bar", "bar", null, "bar2", "bar2"]
#
# Explanation
# TimeMap timeMap = new TimeMap();
# timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
# timeMap.get("foo", 1);         // return "bar"
# timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and
# timestamp 2, then the only value is at timestamp 1 is "bar".
# timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
# timeMap.get("foo", 4);         // return "bar2"
# timeMap.get("foo", 5);         // return "bar2"

# Constraints:
# 1 <= key.length, value.length <= 100
# key and value consist of lowercase English letters and digits.
# 1 <= timestamp <= 107
# All the timestamps timestamp of set are strictly increasing.
# At most 2 * 105 calls will be made to set and get.


# Binary Search (Floor Find Variant) via Hash Map Array Storage.
import bisect


class TimeMap:

    def __init__(self):
        """Initializes the data structure."""
        # Map keys to a list of tuples: key -> [(timestamp1, value1), (timestamp2, value2), ...]
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        """Stores the key with the value at the given timestamp."""
        if key not in self.store:
            self.store[key] = []
        # Timestamps arrive in strictly increasing order, keeping the list sorted automatically
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        """Returns the value associated with the largest timestamp_prev <= timestamp."""
        if key not in self.store:
            return ""

        pairs = self.store[key]

        # Binary search for the insertion point of a dummy tuple with the target timestamp.
        # We append a dummy string to match the tuple structure.
        # bisect_right finds the first element greater than the target timestamp.
        idx = bisect.bisect_right(pairs, (timestamp, chr(127)))

        # If the index is 0, it means all stored timestamps are strictly greater than the target
        if idx == 0:
            return ""

        # The correct floor entry is at index idx - 1
        return pairs[idx - 1][1]


if __name__ == "__main__":
    time_map = TimeMap()

    # 1. Insert values at different timestamps
    time_map.set("foo", "bar", 1)
    print("Set 'foo' to 'bar' at timestamp 1")

    # 2. Lookup values
    print(f"Get 'foo' at timestamp 1: {time_map.get('foo', 1)}")  
    # Output: "bar"
    print(f"Get 'foo' at timestamp 3: {time_map.get('foo', 3)}")  
    # Output: "bar" (Floor lookup finds timestamp 1)

    # 3. Add an updated value
    time_map.set("foo", "bar2", 4)
    print("Set 'foo' to 'bar2' at timestamp 4")

    # 4. Lookup subsequent values
    print(f"Get 'foo' at timestamp 4: {time_map.get('foo', 4)}")  
    # Output: "bar2"
    print(f"Get 'foo' at timestamp 5: {time_map.get('foo', 5)}")  
    # Output: "bar2"
    print(f"Get 'foo' at timestamp 0: {time_map.get('foo', 0)}")  
    # Output: "" (No timestamps exist <= 0)


# Time Complexity:
# 	• set(): O(1) constant time complexity. Appending an item to a dynamic array or hash map bucket map happens
# 	in amortized constant operations.
# 	• get(): O(log M), where M is the number of values stored under the specified key. Finding the insertion boundary
# 	inside the sorted tuple timeline executes using a binary look-up scale.
# Space Complexity: O(N) auxiliary space total, where N represents the total number of key-value-timestamp records
# inserted into the TimeMap layout structure overall.
