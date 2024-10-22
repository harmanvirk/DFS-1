# Time Complexity = O(m*n) | Space Complexity = O(m*n)

from collections import deque
class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        row = len(image)
        col = len(image[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        old_color = image[sr][sc]
        if old_color == color: return image

        queue = deque()
        queue.append((sr, sc))
        image[sr][sc] = color

        while len(queue) != 0:
            curr = queue.popleft()
            for d in dirs:
                nr = curr[0] + d[0]
                nc = curr[1] + d[1]
                if nr >= 0 and nc >= 0 and nr < row and nc < col and image[nr][nc] == old_color:
                    image[nr][nc] = color
                    queue.append((nr, nc))

        return image


# Time Complexity = O(m*n) | Space Complexity = O(m*n)
class DFSSolution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        self.row = len(image)
        self.col = len(image[0])
        self.dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        old_color = image[sr][sc]
        if old_color == color: return image

        self.dfsHelper(image, sr, sc, color, old_color)

        return image

    def dfsHelper(self, image: list[list[int]], i: int, j: int, c: int, oc: int):
        # base case

        # logic
        image[i][j] = c
        for d in self.dirs:
            nr = i + d[0]
            nc = j + d[1]
            if nr >= 0 and nc >= 0 and nr < self.row and nc < self.col and image[nr][nc] == oc:
                self.dfsHelper(image, nr, nc, c, oc)




