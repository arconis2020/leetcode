import cProfile
import random
from string import ascii_lowercase
from collections import Counter


class Solution:
    def minDeletions(self, s: str) -> int:
        counts = Counter(s)
        seen = set()
        deletions = 0
        for _, cnt in counts.most_common():
            while cnt in seen and cnt > 0:
                deletions += 1
                cnt -= 1
            seen.add(cnt)
        return deletions


if __name__ == "__main__":
    s = random.choices(ascii_lowercase, k=10**5)
    sol = Solution()
    pr = cProfile.Profile()
    pr.enable()
    for _ in range(1000):
        sol.minDeletions(s)
    pr.disable()
    pr.dump_stats("./stats")
