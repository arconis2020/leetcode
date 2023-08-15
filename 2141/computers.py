class Solution:
    def checkTime(self, runtime: int) -> int:
        energy_req = runtime * self.n
        energy_avail = sum([min(x, runtime) for x in self.batteries])
        if energy_req > energy_avail:  # Reduce runtime.
            return -1  # Move left
        if energy_req <= energy_avail:  # Increase runtime.
            return 1  # Move right

    def binsearch(self, l=1, r=10**9):
        guess = r - ((r - l) // 2)
        res = self.checkTime(guess)
        if res == -1:  # Move left
            r = guess
        if res == 1:  # Move right
            l = guess
        if res == 0:
            return guess
        nextguess = r - ((r - l) // 2)
        if nextguess == guess:  # you've hit the limit, test the range.
            for x in range(l, r+1):
                res = self.checkTime(x)
                if res <= 0:  # At the first non-right move
                    return x + res
        return self.binsearch(l, r)

    def maxRunTime(self, n: int, batteries: list[int]) -> int:
        self.n = n
        self.batteries = batteries
        max_runtime = (sum(batteries) // n) + 1
        return self.binsearch(l=1, r=max_runtime)
