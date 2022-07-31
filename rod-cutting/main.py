class Solution:
    def setup(self, n: int):
        self.memory = [-1] * (n+1)

    def rcsv(self, n: int, prices: [int]) -> int:
        if n <= 0:
            return 0
        if self.memory[n] != -1:
            return self.memory[n]
        if n == 1:
            return prices[0]
        _max = 0
        _len = len(prices)
        for i in range(1, n+1):
            if i < _len:
                _max = max(prices[i-1] + self.rcsv(n-i, prices), _max)
        self.memory[n] = _max
        return _max

    def maximumProfit(self, n: int, prices: [int]) -> int:
        self.setup(n)
        return self.rcsv(n, prices)


A = [1, 3, 4, 5, 7, 9, 10, 11]
n = 8

solution = Solution()
print(solution.maximumProfit(8, A))
