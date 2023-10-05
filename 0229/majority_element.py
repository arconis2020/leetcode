import cProfile
import random


"""
TAKEAWAYS:
    1. The trivial counter solution is faster than my naive implementation of Boyer-Moore.
    2. This implementation of Boyer-Moore works, but is more complex than it needs to be.
    3. You can literally use Boyer-Moore with 2 majority pointers and two vote counters. 
    4. This method is still academically interesting even if it isn't as fast.
"""

class Solution:
    def __init__(self):
        """Instantiate some attributes."""
        self.n = 0
        self.nums = None
        self.left = None
        self.right = None

    def mooreVote(self, direction):
        """Use Moore's voting algorithm to find the majority of a half."""
        if direction == "left":
            votes = self.left
        else:
            votes = self.right
        m = None
        i = 0
        for vote in votes:
            if i == 0:
                m = vote
                i = 1
            elif m == vote:
                i += 1
            else:
                i -= 1
        return m

    def partition(self, direction="left"):
        """Partition the main list into 2 halves without splitting a group."""
        middle = self.n // 2
        split = middle
        for i in range(1, middle):
            if self.nums[middle - i] != self.nums[middle]:
                split = middle - i
                break
            if self.nums[middle + i] != self.nums[middle]:
                split = middle + i
                break
        self.left = self.nums[:split]
        self.right = self.nums[split:]

    def majorityElement(self, nums: list[int]) -> list[int]:
        """Sort the list, split it in half, and grab the majorities (there can be max 2)."""
        self.n = len(nums)
        self.nums = sorted(nums)
        result = []
        target = (self.n // 3) + 1
        # Handle the edge cases:
        if self.n < 2:
            return nums
        self.partition()
        left_maj = self.mooreVote("left")
        right_maj = self.mooreVote("right")
        # Confirm the majorities meet criteria.
        if nums.count(left_maj) >= target:
            result.append(left_maj)
        if nums.count(right_maj) >= target:
            result.append(right_maj)
        # Clean up any duplicates.
        return list(set(result))


if __name__ == "__main__":
    nums = random.choices(range(-(10**9), 10**9 + 1), k=5 * 10**4)
    s = Solution()
    with cProfile.Profile() as pr:
        for _ in range(100):
            s.majorityElement(nums)
        pr.dump_stats("./stats")
