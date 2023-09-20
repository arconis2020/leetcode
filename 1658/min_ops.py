import random
import cProfile


class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        n_len = len(nums)
        msa_total = total = sum(nums)
        msa_target = total - x
        # Early outs
        if n_len == 1 and nums[0] != x:
            return -1
        if x > total:
            return -1
        if x == total:
            return n_len
        if x < nums[0] and x < nums[-1]:
            return -1
        low = high = 0
        count_list = []
        window_sum = 0
        for low in range(n_len):
            while window_sum < msa_target and high < n_len:
                window_sum += nums[high]
                high += 1
            if window_sum == msa_target:
                count_list.append(high - low - 1)
            window_sum -= nums[low]
        return n_len - max(count_list) - 1


if __name__ == "__main__":
    s = Solution()
    nums = random.choices(range(1, 10**4 + 1), k=10**5)
    x = random.choice(range(1, 10**9 + 1))
    with cProfile.Profile() as pr:
        for _ in range(100):
            s.minOperations(nums, x)
        pr.dump_stats("./stats")
