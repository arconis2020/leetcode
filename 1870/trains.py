from math import ceil

class Solution:
    def checkTime(self, speed: int) -> float:
        return sum([ceil(x/speed) for x in self.dist[:-1]]) + (self.dist[-1] / speed)

    def binsearch(self, l=1, r=10**7):
        guess = l + ((r - l) // 2)
        res = self.checkTime(guess)
        if res < self.hour:  # Move left
            r = guess
        if res > self.hour:  # Move right
            l = guess
        if guess == self.hour:
            return guess
        nextguess = l + ((r - l) // 2)
        if nextguess == guess:  # you've hit the limit, test the range.
            for x in range(l, r+1):
                if self.checkTime(x) <= self.hour:
                    return x
        return self.binsearch(l, r)

    def minSpeedOnTime(self, dist: list[int], hour: float) -> int:
        # Handle the impossible case:
        if len(dist) > ceil(hour):
            # Because trains depart on integer hours, each train will cost a minimum of 1 hour.
            return -1  # Impossible
        self.dist = dist
        self.hour = hour
        return self.binsearch()
