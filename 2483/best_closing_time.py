class Solution:
    def bestClosingTime(self, customers: str) -> int:
        clen = len(customers)
        # Set up a tracking list
        penalties = [0] * (clen + 1)
        # Count the penalties for closing late by adding penalties for N's
        count = 0
        for idx, char in enumerate(customers):
            if char == "N":
                count += 1
            penalties[idx + 1] += count
        # Count the penalties for closing early by adding penalties for Y's
        count = 0
        for idx, char in enumerate(reversed(customers)):
            if char == "Y":
                count += 1
            penalties[clen - 1 - idx] += count
        # Account for closing after all documented hours.
        lowest = min(penalties)
        return penalties.index(lowest)
