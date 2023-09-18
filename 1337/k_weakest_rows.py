import cProfile


class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        # Establishing a list of specific length is faster than using .append.
        result = [None] * len(mat)
        for idx, row in enumerate(mat):
            # Rolling my own counter of 1s is faster than using takewhile from itertools.
            strength = 0
            for n in row:
                if n == 1:
                    strength += 1
                else:
                    break
            # Strength in the front allows for easy sorting of the list without a key.
            result[idx] = (strength, idx)
        # Sorting and truncating is faster than using heapq.nsmallest.
        return [x[1] for x in sorted(result)[:k]]


if __name__ == "__main__":
    mat = [[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]]
    k = 3
    s = Solution()
    with cProfile.Profile() as pr:
        for _ in range(100000):
            s.kWeakestRows(mat, k)
        pr.dump_stats("./stats")
