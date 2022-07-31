class Solution:
    def numDecodings(self, st: str) -> int:
        n = len(st)
        if n == 0:
            return 0
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1
        if st[0] == '0':
            return 0
        for i in range(2, n+1):
            one = int(st[i-1:i])
            two = int(st[i-2:i])
            if one > 0 and one < 10:
                _one = dp[i-1]
            else:
                _one = 0
            if two > 9 and two < 27:
                _two = dp[i-2]
            else:
                _two = 0
            dp[i] = _two + _one

        return dp[n]


import time

solution = Solution()
file = open("argument", "r")
string = int(file.read(10000+10))
string = str(string)
s = time.time()
result = solution.numDecodings(string)
e = time.time()
print(result)
print(e-s)
