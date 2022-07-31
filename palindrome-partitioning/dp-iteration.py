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

    def getPartitions(self, s: str):
        s = s[::-1]
        self.getPartitionsSum(s)
        dp = self.dp
        j = len(s) - 1
        stack = []
        # initial pushing
        for i in range(j+1):
            if dp[i][j] == 1:
                new = self.newFrame(i, j)
                stack.append(new)
        while len(stack) > 0:
            frame = stack.pop()
            # print(frame)
            n = frame['n']
            m = frame['m']
            if frame['flag'] == 1:
                # deal with this one 
                self.li.append(s[n: m+1])
                frame['flag'] = 0
                # stack it again to pop later
                stack.append(frame)
                # push children into stack
                if n > 0:
                    self.inStack(stack, n-1)
                elif n == 0:
                    tmp = self.li[:]
                    self.results.append(tmp)
            elif frame['flag'] == 0:
                self.li.pop()
                frame['flag'] = -1
        return self.results

    def newFrame(self, n, m):
        frame = {
            'n': n,
            'm': m,
            'flag': 1
        }
        return frame

    def inStack(self, stack, j):
        dp = self.dp
        for i in range(j+1):
            if dp[i][j] == 1:
                new = self.newFrame(i, j)
                stack.append(new)


solution = Solution()
s = 'abdjfrururhcdchahjkljldfasfjljbvcxiojkwjrqneksdfaenduhad'
s = 'acdca'
n = len(s)
import sys
if len(sys.argv) == 2:
    s = sys.argv[1]
import time
start = time.time()
# solution.getPartitionsSum(s)
solution.getPartitions(s)
end = time.time()
print(solution.results)
print("time elapsed: ", end-start)
