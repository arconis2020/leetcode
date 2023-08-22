from string import ascii_uppercase


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        n = columnNumber
        while n != 0:
            n -= 1  # Deal with 0 indexing
            n, rem = divmod(n, 26)
            res += ascii_uppercase[rem]
        return res[::-1]
