import cProfile
import random
from collections import Counter


class Solution:
    def findDuplicateList(self, nums):
        """
        Detect numbers using indices and boolean tracking.
        O(n) time
        O(n) space
        """
        check = [False] * len(nums)
        for n in nums:
            if not check[n]:
                check[n] = True
            else:
                return n

    def findDuplicateCounter(self, nums):
        """
        Simple count and report.
        O(n) time
        O(n) space
        """
        c = Counter(nums)
        return c.most_common(1)[0][0]

    def findDuplicate(self, nums: list[int]) -> int:
        """
        Use the indices as the nodes, and the values as the pointers to other indices
        Floyd's cycle detection
        O(n) time
        O(1) space
        """
        (slow, fast) = (0, 0)
        while True:
            slow = nums[slow]  # .next
            fast = nums[nums[fast]]  # .next.next
            if slow == fast:
                slow = 0
                while slow != fast:
                    slow = nums[slow]
                    fast = nums[fast]
                return slow



if __name__ == "__main__":
    nums = list(range(1, 10**5 + 1))
    random.shuffle(nums)
    dupe = random.choice(nums)
    dupeidx = random.choice(nums)
    nums.insert(dupeidx, dupe)
    s = Solution()
    with cProfile.Profile() as pr:
        for _ in range(100):
            s.findDuplicate(nums)  # Fast
            s.findDuplicateCounter(nums)  # Faster
            s.findDuplicateList(nums)  # Fastest
        pr.dump_stats("./stats")
