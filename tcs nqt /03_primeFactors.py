import math

class Solution:

    def AllPrimeFactors(self, N):
        # Set to store unique prime factors
        prime_factors = set()
        
        # Check for the number of 2's that divide N
        while N % 2 == 0:
            prime_factors.add(2)
            N = N // 2
        
        # Check for odd numbers from 3 to sqrt(N)
        for i in range(3, int(math.sqrt(N)) + 1, 2):
            while N % i == 0:
                prime_factors.add(i)
                N = N // i
        
        # If N is still greater than 2, it must be a prime number
        if N > 2:
            prime_factors.add(N)
        
        # Return a sorted list of unique prime factors
        return sorted(prime_factors)
