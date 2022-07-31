class JewelStone:
    def __init__(self, weight=0, value=0):
        self.weight = weight
        self.value = value


class Solution:
    def getMaxValue(self, stones: [JewelStone], capacity: int) -> int:
        n = len(stones)
        dp = [[0]*(capacity+1) for i in range(n+1)]
        for i in range(1, n+1):
            w = stones[i-1].weight
            v = stones[i-1].value
            for j in range(1, capacity+1):
                if j >= w:
                    dp[i][j] = max(dp[i-1][j-w] + v, dp[i-1][j])
                else:
                    dp[i][j] = dp[i-1][j]

        return dp[n][capacity]


li = [(1, 3), (2, 4), (3, 5), (4, 7)]
stones = []

for i in li:
    stones.append(JewelStone(weight=i[0], value=i[1]))


solution = Solution()
print(solution.getMaxValue(stones, 5))
