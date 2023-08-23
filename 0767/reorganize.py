from collections import Counter


class Solution:
    def reorganizeString(self, s: str) -> str:
        s_len = len(s)
        c = Counter(s)
        if c.most_common(1)[0][1] > (s_len + 1) // 2:
            return ""
        res = []
        last = ""
        while len(res) < s_len:
            append_list = [x[0] for x in c.most_common(2)]
            res.extend(append_list)
            c.subtract(append_list)
            c = +c  # Remove zero-count fields
            last = append_list[-1]
        return "".join(res)
