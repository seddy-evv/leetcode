# To get the top five largest integers from a list in Python, the most efficient and standard way is to use the heapq.nlargest() 
# function from the built-in library, or the sorted() function for simpler use cases.

# Here are the best methods to achieve this:
# Method 1: Using heapq.nlargest (Best for large lists)
# This method is highly optimized because it does not sort the entire list, saving memory and time.
import heapq

numbers = [45, 12, 89, 5, 100, 67, 23, 90, 11]

# Get the 5 largest numbers
top_five = heapq.nlargest(5, numbers)

print(top_five)
# Output: [100, 90, 89, 67, 45]

# Method 2: Using sorted() slicing (Best for small lists)
# You can sort the list in descending order and slice the first five elements.
numbers = [45, 12, 89, 5, 100, 67, 23, 90, 11]

# Sort descending and take the first 5
top_five = sorted(numbers, reverse=True)[:5]

print(top_five)
# Output: [100, 90, 89, 67, 45]


# Quick Comparison:
# - heapq.nlargest: Runs in O(Nlog K) time. It is much faster if your list has thousands of items.
# - sorted(): Runs in O(Nlog N) time. It is perfectly fine for smaller, everyday lists.
