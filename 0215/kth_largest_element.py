# from heapq import nlargest
# 
# 
# class Solution:
#     def findKthLargest(self, nums: list[int], k: int) -> int:
#         return nlargest(k, nums)[-1]
# 

from random import getrandbits


class Solution:
    def partition(self, left, right, pivot):
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

    def select(self, left, right, k):
        """Find the kth-largest value (self.n-smallest value) in the partitioned list."""
        if left >= right:
            return self.nums[left]
        pivot = left + (getrandbits(16) % (right - left + 1))
        pivot = self.partition(left, right, pivot)
        if self.n == pivot:
            return self.nums[self.n]
        if self.n < pivot:
            return self.select(left, pivot - 1, k)
        return self.select(pivot + 1, right, k)

    def findKthLargest(self, nums: list[int], k: int) -> int:
        self.nums = nums
        self.n = len(nums) - k
        return self.select(0, len(nums) - 1, k)
