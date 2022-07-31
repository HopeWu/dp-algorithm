class Solution:
    def assign(self, s1: str, s2: str):
        self.s1 = s1
        self.s2 = s2
        self.l1 = len(s1)
        self.l2 = len(s2)
        self.dp = [[0 for j in range(self.l2)] for i in range(self.l1)]

    def rcrsv(self, p1, p2):
        if p1 > self.l1 - 1 and p2 > self.l2 - 1:
            return 0
        if p1 > self.l1 - 1 and p2 <= self.l2 - 1:
            return self.l2 - 1 - p2 + 1
        if p2 > self.l2 - 1 and p1 <= self.l1 - 1:
            return self.l1 - 1 - p1 + 1

        if self.dp[p1][p2] != 0:
            return self.dp[p1][p2]

        if self.s1[p1] == self.s2[p2]:
            result = self.rcrsv(p1+1, p2+1)
            self.dp[p1][p2] = result
            return result
        else:
            result = min(1 + self.rcrsv(p1+1, p2),
                         1 + self.rcrsv(p1+1, p2+1),
                         1 + self.rcrsv(p1, p2+1))
            self.dp[p1][p2] = result
            return result

    def minOperations(self, s1: str, s2: str) -> int:
        self.assign(s1, s2)
        return self.rcrsv(0, 0)


solution = Solution()


s1 = "hello"
s2 = "seldom"
print(solution.minOperations(s1, s2))
s1 = "workattech"
s2 = "workattech"
print(solution.minOperations(s1, s2))
s1 = "abc"
s2 = "def"
print(solution.minOperations(s1, s2))
s1 = "ab"
s2 = "ba"
print(solution.minOperations(s1, s2))
s1 = "workat"
s2 = "word"
print(solution.minOperations(s1, s2))
