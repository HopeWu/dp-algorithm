class Solution:
    def build(self):
        s = self.s
        dp = self.dp
        n = len(s)
        # initiating
        for i in range(n):
            dp[i][i] = 1
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = 1
        for i in range(n-3, -1, -1):
            for j in range(i+2, n):
                if s[i] == s[j] and dp[i+1][j-1] == 1:
                    dp[i][j] = 1

    def getPartitionsSum(self, s: str) -> [[str]]:
        self.setup(s)
        self.build()
        n = len(s)
        # print(self.dp)
        dp2 = self.dp
        dp = [0]*(n+1)
        dp[0] = 1
        for j in range(1, n+1):
            for i in range(j):
                if dp2[i][j-1] == 1:
                    dp[j] += dp[i]
        return dp[n]

    def setup(self, s: str):
        self.s = s
        self.li = []
        self.results = []
        n = len(s)
        self.dp = [[0]*n for i in range(n)]

    def _getPartitions(self, j):
        s = self.s
        if j == 0:
            self.li.append(s[0])
            tmp = self.li[:]
            self.results.append(tmp)
            self.li.pop()
            return
        if j == -1:
            tmp = self.li[:]
            self.results.append(tmp)
            return
        if j < 0:
            return
        dp = self.dp
        for i in range(j+1):
            if dp[i][j] == 1:
                self.li.append(s[i: j+1])
                self._getPartitions(i-1)
                self.li.pop()

    def getPartitions(self, s: str):
        s = s[::-1]
        self.getPartitionsSum(s)
        n = len(s) - 1
        self._getPartitions(n)
        return self.results


solution = Solution()
s = 'abdjfrururhcdchahjkljldfasfjljbvcxiojkwjrqneksdfaenduhad'
s = 'cdc'
#s = 'acdca'
n = len(s)
import time
start = time.time()
solution.getPartitions(s)
end = time.time()
print(solution.results)
print("time elapsed: ", end-start)
print(s)
