from collections import defaultdict


class Solution:
    def findSmallestInteger(self, nums: list[int], value: int) -> int:
        # First build a dict with all of the smallest possible result values.
        valid_ints = defaultdict(int)  # integer -> Count of this integer.
        for num in nums:
            # Remainder is the lowest possible int you can make with this combo.
            valid_ints[num % value] += 1
        """
        Now fill in the intermediate values between X and X+Value*n
          - X is one of the keys from valid_ints.
          - n is the number of times that integer can be used in the list.
        """
        for key in list(valid_ints.keys()):
            n = 1
            while n < valid_ints[key]:
                intermediate = key + n * value
                valid_ints[intermediate] = 1
                n += 1
        # Now that we have all possible valid integers, guess from 0 until you find the gap.
        guess = 0
        while guess in valid_ints:
            guess += 1
        return guess
