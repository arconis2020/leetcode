from collections import defaultdict


class Solution:
    def groupThePeople(self, groupSizes: list[int]) -> list[list[int]]:
        retlist = []
        idxs_by_size = defaultdict(list)
        for idx, g_size in enumerate(groupSizes):
            idxs_by_size[g_size].append(idx)
        for g_size, idx_list in idxs_by_size.items():
            groups = [idx_list[x:x+g_size] for x in range(0, len(idx_list), g_size)]
            retlist.extend(groups)
        return retlist
