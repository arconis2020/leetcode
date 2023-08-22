from collections import deque

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        wordDict = dict.fromkeys(wordDict)  # Searches go from O(len(wordDict)) to O(1)
        slen = len(s)
        stops = deque([0])
        used = {}
        while stops:
            l = stops.popleft()
            r = l + 1
            while r <= slen:
                test_str = s[l:r]
                if test_str in wordDict:
                    # Early out: If r == len(s) on a valid word, you hit the goal.
                    if r == slen:
                        return True
                    if r not in used:
                        stops.append(r)
                    used[r] = None  # We can't use the same path twice.
                r += 1
        # Did len(s) end up as the last stop?
        return l == slen
