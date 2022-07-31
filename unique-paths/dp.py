class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1:
            return 1
        if n == 1:
            return 1
        dp = [[0]*n for i in range(m)]
        dp[m-2][n-1] = 1
        dp[m-1][n-2] = 1
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m-1 and j == n-1:
                    continue
                if i == m-2 and j == n-1:
                    continue
                if i == m-1 and j == n-2:
                    continue
                if i + 1 < m:
                    right = dp[i+1][j]
                else:
                    right = 0
                if j + 1 < n:
                    down = dp[i][j+1]
                else:
                    down = 0
                dp[i][j] = right + down
        return dp[0][0]


import time

solution = Solution()
s = time.time()
result = solution.uniquePaths(2, 2)
e = time.time()
print(result)
print(e-s)
