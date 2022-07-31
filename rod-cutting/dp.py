class Solution:
    def maximumProfit(self, n: int, prices: [int]) -> int:
        dp = [0] * (n+1)
        dp[1] = prices[0]
        for i in range(2, n+1):
            _max = 0
            for j in range(1, i+1):
                _max = max(_max, prices[j-1] + dp[i-j])
            dp[i] = _max
        return dp[n]


A = [1, 3, 4, 5, 7, 9, 10, 11]
n = 8

solution = Solution()
print(solution.maximumProfit(8, A))
