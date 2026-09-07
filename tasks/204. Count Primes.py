# Given an integer n, return the number of prime numbers that are strictly less than n.A prime number is a natural number
# strictly greater than 1 that has no positive divisors other than 1 and itself (e.g., 2, 3, 5, 7, 11...).

# Examples
# Example 1:Input: n = 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, 
# which are 2, 3, 5, and 7.

class Solution:
    def countPrimes(self, n: int) -> int:
        # Base case: There are no primes strictly less than 2
        if n <= 2:
            return 0
            
        # Initialize the sieve array. True indicates a potential prime number.
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime
        
        # We only need to iterate up to the square root of n
        for p in range(2, int(n**0.5) + 1):
            if is_prime[p]:
                # Mark all multiples of p starting from p*p as composite (False)
                # The step size is p
                for multiple in range(p * p, n, p):
                    is_prime[multiple] = False
                    
        # The sum of True values gives the count of primes less than n
        return sum(is_prime)

# --- Quick Interview Verification ---
sol = Solution()
print(sol.countPrimes(10))  # Output: 4 (Primes: 2, 3, 5, 7)
print(sol.countPrimes(50))  # Output: 15
