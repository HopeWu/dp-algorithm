class Solution:
    # add your logic here
    def getLengthOfLIS(self, A) -> int:
        _max = 0
        for i in range(len(A)):
            self.length = 0
            self.result = []
            _max = max(_max, self.reGetLengthOfLIS(A, i))
        return _max


a = [10, 20, 2, 5, 3, 8, 8, 25, 6]
b = [10, -63, 7, -50, 32, -9, -3]
c = [71, 0, 4, 42, -31, 4, -42]
d = [77, 0, -2, 25, 1, 70]
e = [2, 2, 1, 5, 7, -50, 80]


obj = Solution()

print(obj.getLengthOfLIS(a))
print(obj.getLengthOfLIS(b))
print(obj.getLengthOfLIS(c))
#obj.printDict(c)
print(obj.getLengthOfLIS(d))
print(obj.getLengthOfLIS(e))
