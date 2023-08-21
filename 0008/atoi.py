from string import digits

class Solution:
    def myAtoi(self, s: str) -> int:
        result = ""
        positive = True
        # Strip leading whitespace. ONLY leading whitespace.
        s = s.lstrip()
        if not s:  # Handle the 0-length case.
            return 0
        # Check for -/+.
        if s[0] == "-":
            positive = False
            s = s[1:]
        elif s[0] == "+":
            s = s[1:]
        # Handle the special case where you've hit the EOS already.
        if not s:
            return 0
        # Read in digits until the next non-digit or EOS.
        for char in s:
            if char in digits:
                result += char
            else:
                break  # Stop reading at the first non-digit.
        # If no digits were read, then the integer is 0.
        if not result:
            return 0
        # Convert to integer, clamping to the limits of 32-bit signed ints.
        if positive:
            return min(int(result), 2**31-1)
        # Must be negative.
        return max(-2**31, -int(result))
