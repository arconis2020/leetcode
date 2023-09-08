import cProfile


class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        result = [[1],[1,1]]
        for n in range(3, numRows + 1):
            this_row = [1] * n
            for m in range(1, n - 1):
                this_row[m] = result[-1][m - 1] + result[-1][m]
            result.append(this_row)
        return result if numRows > 1 else result[:1]


if __name__ == "__main__":
    s = Solution()
    pr = cProfile.Profile()
    pr.enable()
    for _ in range(10000):
        s.generate(30)
    pr.disable()
    pr.dump_stats("./stats")
