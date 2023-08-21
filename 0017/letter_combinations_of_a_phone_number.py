class Solution:
    t9 = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
    }

    def backtrack(self, first=0, curr=[]):
        # When you find a valid combination.
        if len(curr) == self.dlen:
            self.output["".join(curr)] = None
            return
        # Iterate over the original string, with each recursion advancing.
        for digit in self.digits[first:]:
            # Special to T9 texting: A combo is only valid if the T9 substitutions are in the proper order.
            if self.digits[len(curr)] != digit:
                continue
            # Iterate from 0 to the longest substitution list length.
            for i in range(self.max):
                try:
                    # Add the substitution to the work list, or
                    curr.append(self.t9[digit][i])
                except IndexError:
                    # Skip adding anything for this index because it doesn't exist in the T9 sub
                    continue
                # Recurse to the next level.
                self.backtrack(first + 1, curr)
                # After recursion, backtrack.
                curr.pop()

    def letterCombinations(self, digits: str) -> list[str]:
        # Set a globally accessible digits value.
        self.digits = digits
        # Set a globally accessible length of each combo.
        self.dlen = len(digits)
        # Make sure output is unique.
        self.output = {}
        # Handle the empty string case first.
        if not digits:
            return []
        # Set a globally accessible limit for the number of inner-loops in backtrack.
        self.max = max([len(x) for x in self.t9.values()])
        # Backtrack
        self.backtrack()
        # Return an actual list as required.
        return list(self.output.keys())
