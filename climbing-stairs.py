# LeetCode No. 70, Climbing Stairs.
# Solved using the fact that the results follow the fibonacci sequence.
class Solution(object):
    
    def fib(self, n):
        
        if n < len(self.cache):
            return self.cache[n]
        y = self.fib(n-1) + self.fib(n-2)
        self.cache.append(y)
        return y
    def climbStairs(self, n):
        self.cache = [0, 1]
        """
        :type n: int
        :rtype: int

        is fibonacci sequence
        """
        x = self.fib(n+1)
        return(x)
    
