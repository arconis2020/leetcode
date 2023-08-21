class Solution:
    def getFactors(self, i):
        return [n for n in range(1, (i // 2) + 1) if not i % n]

    def checkStringLength(self, i):
        return self.s[:i] * (self.s_len // i) == self.s

    def repeatedSubstringPattern(self, s: str) -> bool:
        self.s_len = len(s)
        self.s = s
        # Single-character strings are not substringable
        if self.s_len < 2:
            return False
        lengths = self.getFactors(self.s_len)
        for l in lengths:
            if self.checkStringLength(l):
                return True
        return False
