class Solution:
    def maxProduct(self, A: [int]) -> int:
        n = len(A)
        if n == 1:
            return A[0]
        # dp = [[float('-inf')]*(n) for i in range(n-1)]
        # dp = [float('-inf')]*(n)

        _max = float('-inf')
        for i in range(n-1):
            for j in range(i+1, n):
                if j == i+1:
                    curr = A[i] * A[j]

                if j > i+1:
                    curr = prev * A[j]

                if curr > _max:
                    _max = curr

                prev = curr


        return _max


solution = Solution()
s = "-2"
A = s.split(' ')
A = [int(i) for i in A]
print(solution.maxProduct(A))
