class Solution:
    def romanToInt(self, s: str) -> int:
        valmap = {
            "I": {"V": 4, "X": 9, "*": 1},
            "V": {"*": 5},
            "X": {"L": 40, "C": 90, "*": 10},
            "L": {"*": 50},
            "C": {"D": 400, "M": 900, "*": 100},
            "D": {"*": 500},
            "M": {"*": 1000},
        }
        value = 0
        chars = list(s)
        while chars:
            this_char = chars.pop(0)
            this_valdict = valmap[this_char]
            if not chars:
                value += this_valdict["*"]
                continue
            next_char = chars[0]
            if next_char in this_valdict:
                value += this_valdict[next_char]
                chars.pop(0)
            else:
                value += this_valdict["*"]
        return value
