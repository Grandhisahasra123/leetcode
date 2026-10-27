class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = [['#'] * n for _ in range(m)]
        for j in range(n):
            grid[0][j] = '.'
        for i in range(1, m):
            grid[i][n - 1] = '.'
        for i in range(1, m):
            for j in range(n - 1):
                grid[i][j] = '#'
        return [''.join(row) for row in grid]