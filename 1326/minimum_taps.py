class Solution:
    def minTaps(self, n: int, ranges: list[int]) -> int:
        distances = {}
        for idx, tap in enumerate(ranges):
            """
            Don't use min/max here to limit the range from 0-n.
            In the limit case, it slows things down by 25% compared
            to this simple if statement for 0 and no limit on the right.
            """
            if tap >= idx:
                left = 0
            else:
                left = idx - tap
            right = idx + tap
            """
            Don't use the safety function distances.get(left, 0).
            Using the "in" function and direct comparison is significantly faster.
            """
            if left not in distances:
                distances[left] = right
                continue
            if right > distances[left]:
                distances[left] = right
        # Start from 0
        left = 0
        try:
            right = distances[0]
        except KeyError:
            return -1
        count = 1
        # Find the next overlapping tap
        while right < n:
            max_right = right
            max_left = left
            for i in range(right, left - 1, -1):
                if i not in distances:
                    continue
                new_right = distances[i]
                if new_right > max_right:
                    max_left = i
                    max_right = new_right
            # If there is no overlapping tap.
            if max_right == right:
                return -1
            count += 1
            left = max_left
            right = max_right
        return count
