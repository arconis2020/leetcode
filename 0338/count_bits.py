from functools import lru_cache


class Solution:
    @lru_cache(maxsize=None)
    def recursiveGetBits(self, i):
        if i == 0:
            return 0
        if i == 1:
            return 1
        i, rem = divmod(i, 2)
        return rem + self.recursiveGetBits(i)

    def countBits(self, n: int) -> list[int]:
        return [self.recursiveGetBits(x) for x in range(n + 1)]
