from collections import deque


class Solution:
    def getNeighbors(self, x, y):
        neighbors = []
        if x < self.m - 1:
            neighbors.append((x+1, y))
        if x > 0:
            neighbors.append((x-1, y))
        if y < self.n - 1:
            neighbors.append((x, y+1))
        if y > 0:
            neighbors.append((x, y-1))
        return neighbors

    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        self.m = len(mat)
        self.n = len(mat[0])
        queue = deque()
        processed = set()
        distances = [[None] * self.n for _ in range(self.m)]
        # Set up the zeros first
        for x in range(self.m):
            for y in range(self.n):
                node = mat[x][y]
                if node == 0:
                    distances[x][y] = 0
                    queue.append((x,y))
        while queue:
            node = queue.popleft()
            processed.add(node)
            x, y = node
            distance = distances[x][y]
            neighbors = self.getNeighbors(x, y)
            for n in neighbors:
                if distances[n[0]][n[1]] is None:
                    distances[n[0]][n[1]] = distance + 1
                if n not in processed:
                    queue.append(n)
        return distances
