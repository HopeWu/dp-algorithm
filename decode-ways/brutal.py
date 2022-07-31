class Solution:
    def setup(self, st):
        self.n = len(st)
        self.st = st[:]

    def rcrsv(self, n: int):


    def numDecodings(self, st: str) -> int:
        self.setup()
        result = self.rcrsv(self.n)
        return result


solution = Solution()
file = open("argument", "r")
string = file.read(10000+10)
result = solution.numDecodings(string)
print(result)
