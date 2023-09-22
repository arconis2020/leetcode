import random
import cProfile
from string import ascii_lowercase


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        start = 0
        for char in s:
            start = t.find(char, start) + 1
            if start == 0:
                return False
        return True


if __name__ == "__main__":
    s = "".join(random.choices(ascii_lowercase, k=100))
    t = "".join(random.choices(ascii_lowercase, k=10**4))
    sol = Solution()
    with cProfile.Profile() as pr:
        for _ in range(100000):
            sol.isSubsequence(s, t)
        pr.dump_stats("./stats")
