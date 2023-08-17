from math import factorial
from random import shuffle

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        pcnt = factorial(len(nums))
        seen = {}
        # Just shove a bezoar down their throat.
        while len(seen) < pcnt:
            seen[tuple(nums)] = None
            shuffle(nums)
        return [list(x) for x in seen.keys()]
