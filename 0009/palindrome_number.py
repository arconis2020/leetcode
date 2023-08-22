class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are never palindromic.
        if x < 0:
            return False
        # Single-digit numbers are always palindromic.
        if x < 10:
            return True
        # Put the digits in a list without converting through strings
        digits = []
        while x != 0:
            x, r = divmod(x, 10)
            digits.append(r)
        # Find the middle of the list.
        midpoint = len(digits) // 2
        # Left and Right will be the same size, and there may be a middle digit.
        left = digits[:midpoint]
        right = digits[-midpoint:]
        return left == list(reversed(right))
