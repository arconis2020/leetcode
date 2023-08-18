from collections import defaultdict
from itertools import combinations


class Solution:
    def maximalNetworkRank(self, n: int, roads: list[list[int]]) -> int:
        roads_by_city = defaultdict(list)
        for road in roads:
            roads_by_city[road[0]].append(tuple(road))
            roads_by_city[road[1]].append(tuple(road))
        max_network_rank = 0
        for origin1, origin2 in combinations(list(roads_by_city.keys()), 2):
            this_network_rank = len(set(roads_by_city[origin1] + roads_by_city[origin2]))
            if this_network_rank > max_network_rank:
                max_network_rank = this_network_rank
        return max_network_rank
