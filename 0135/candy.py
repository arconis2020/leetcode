import random
import cProfile


class Solution:
    def candy(self, ratings: list[int]) -> int:
        r_len = len(ratings)
        if r_len == 0:
            return 0
        if r_len == 1:
            return 1
        candies = [1] * r_len
        for r in range(1, r_len):
            if ratings[r] > ratings[r - 1]:
                candies[r] = candies[r - 1] + 1
        for r in range(r_len - 2, -1, -1):
            if ratings[r] > ratings[r + 1] and candies[r] <= candies[r + 1]:
                candies[r] = candies[r + 1] + 1
        return sum(candies)


if __name__ == "__main__":
    ratings = random.choices(range(2 * 10**4 + 1), k=2 * 10**4)
    s = Solution()
    pr = cProfile.Profile()
    pr.enable()
    for _ in range(100):
        s.candy(ratings)
    pr.disable()
    pr.dump_stats("./stats")
