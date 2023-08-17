from itertools import combinations

class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        proto_list = list(range(1, 1 + n))
        return [list(x) for x in combinations(proto_list, k)]
