# Time Complexity = O(m*n) | Space Complexity = O(m*n)
from collections import deque

class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        row = len(mat)
        col = len(mat[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        queue = deque()
        for i in range(row):
            for j in range(col):
                if mat[i][j] == 0:
                    queue.append((i, j))
                elif mat[i][j] == 1:
                    mat[i][j] = -1

        # dist = 1
        while len(queue) != 0:
            #size = len(queue)
            #for i in range(size):
            curr = queue.popleft()
            for d in dirs:
                nr = curr[0] + d[0]
                nc = curr[1] + d[1]

                if nr >= 0 and nc >= 0 and nr < row and nc < col and mat[nr][nc] == -1:
                    mat[nr][nc] = mat[curr[0]][curr[1]] + 1
                    # mat[nr][nc] = dist
                    queue.append((nr, nc))

            # dist += 1

        return mat

# Time Complexity = O(m*n)  | Space Complexity = O(m*n)
class DFSSolution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        self.m = len(mat)
        self.n = len(mat[0])
        self.result = [[0 for col in range(self.n)] for row in range(self.m)]

        for i in range(self.m):
            for j in range(self.n):
                if mat[i][j] == 1:
                    self.result[i][j] = self.dfsHelper(mat, i, j)

        return self.result


    def dfsHelper(self, mat: list[list[int]], i: int, j: int):
        if i > 0 and mat[i-1][j] == 0: return 1 # top
        if i < self.m -1 and mat[i+1][j] == 0: return 1  # down
        if j > 0 and mat[i][j-1] == 0: return 1  # left
        if j < self.n -1 and mat[i][j+1] == 0: return 1  # right

        top = 9999; left = 9999; bottom = 9999; right = 9999

        if i > 0 and self.result[i-1][j] != 0:
            top = self.result[i-1][j]

        if j > 0 and self.result[i][j-1] != 0:
            left = self.result[i][j-1]

        if j < self.n -1:
            if self.result[i][j+1] == 0:
                self.result[i][j+1] = self.dfsHelper(mat, i, j+1)
            right = self.result[i][j+1]

        if i < self.m - 1:
            if self.result[i+1][j] == 0:
                self.result[i+1][j] = self.dfsHelper(mat, i+1, j)
            bottom = self.result[i+1][j]

        return 1 + min(top, min(left, min(bottom, right)))