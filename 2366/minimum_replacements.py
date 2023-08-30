class Solution:
    def reduce(self, num: int, limit: int):
        ops, rem = divmod(num, limit)
        # If the number is divisible
        if rem == 0:
            self.operations += ops - 1
            return limit
        # If the number is not divisible.
        self.operations += ops
        # The largest possible left-most number will be the below equation because
        # you would split the remainder between all of the indices to your right
        # to maintain sort order. Visualize stacking columns from the right.
        return num // (ops + 1)

    def minimumReplacement(self, nums: list[int]) -> int:
        self.operations = 0
        n_1 = nums[-1]
        for idx in range(len(nums) - 2, -1, -1):
            if nums[idx] > n_1:
                n_1 = self.reduce(nums[idx], n_1)
            else:
                n_1 = nums[idx]
        return self.operations
