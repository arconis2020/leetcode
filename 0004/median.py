import cProfile
import random
from random import getrandbits


class Solution:
    def partition(self, left: int, right: int, pivot: int) -> int:
        """
        Move the pivot index provided to its correct final sort location.

        Everything to the left of the moved pivot index will be smaller than the
        value at that index, but unsorted.
        Everything to the right of the moved pivot index will be larger than the
        value at that index, but unsorted.
        """
        pivot_val = self.nums[pivot]
        self.nums[pivot], self.nums[right] = self.nums[right], self.nums[pivot]
        retval = left
        for i in range(left, right):
            if self.nums[i] < pivot_val:
                self.nums[retval], self.nums[i] = self.nums[i], self.nums[retval]
                retval += 1
        self.nums[right], self.nums[retval] = self.nums[retval], self.nums[right]
        return retval

    def select(self, left: int, right: int, k: int) -> int:
        """Find the kth-smallest value in the partitioned list."""
        if left >= right:
            return self.nums[left]
        pivot = left + (getrandbits(16) % (right - left + 1))
        pivot = self.partition(left, right, pivot)
        if k == pivot:
            return self.nums[k]
        if k < pivot:
            return self.select(left, pivot - 1, k)
        return self.select(pivot + 1, right, k)

    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        """
        Take the divmod(m+n, 2). If not divisible, the result is the median index.
        If divisible, the median indices are result and result-1.

        After finding the correct indices,
        - Add the lists together without sorting.
        - Find the kth smallest element, where k is the index.
        """
        total_len = len(nums1) + len(nums2)
        m_idx, rem = divmod(total_len, 2)
        self.nums = nums1 + nums2
        mid1 = self.select(0, total_len - 1, m_idx)
        if rem == 0:
            mid2 = self.select(0, total_len - 1, m_idx - 1)
            return (mid1 + mid2) / 2
        return float(mid1)


if __name__ == "__main__":
    nums1 = random.choices(range(-10**6, 10**6 + 1), k=1000)
    nums2 = random.choices(range(-10**6, 10**6 + 1), k=1000)
    s = Solution()
    with cProfile.Profile() as pr:
        for _ in range(1000):
            s.findMedianSortedArrays(nums1, nums2)
        pr.dump_stats("./stats")
