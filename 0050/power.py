"""Original binary exponentiation."""
from functools import reduce


class Solution:
    def mult(self, a: float, b: float) -> float:
        return a * b

    def myExp(self, x: float, n: int) -> float:
        # Handle special exponents
        if n == 0:
            return 1
        if n == 1:
            return x
        if n < 0:
            return 1.0 / self.myExp(x, -1 * n)
        # Perform sliding exponent division
        for i in range(10, 1, -1):
            if n % i == 0:  # If this integer is a good divisor for the exp.
                newexp = n / i
                newbase = reduce(self.mult, [x] * i)
                return self.myExp(newbase, newexp)

    def myPow(self, x: float, n: int) -> float:
        return self.myExp(x, n)
