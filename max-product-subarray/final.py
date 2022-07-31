class Solution:
    def maxProduct(self, A: [int]) -> int:
        neg = A[0]
        pos = A[0]
        flag = 0
        _max = A[0]
        _flag = 1
        for i in A:
            if _flag == 1:
                _flag = 0
                continue
            if i == 0:
                flag = 1
                continue

            if i > 0:
                if flag == 1:
                    pos = i
                    neg = i
                elif flag == 0:
                    if pos > 0:
                        pos *= i
                    if pos < 0:
                        pos = i
                    if neg < 0:
                        neg *= i

            if i < 0:
                if flag == 1:
                    neg = i
                    pos = i
                elif flag == 0:
                    tmp = neg
                    if pos > 0:
                        neg = i * pos
                    if tmp < 0:
                        pos = i * tmp

            if flag == 1:
                flag = 0

            _max = max(_max, pos, neg)

        return _max


solution = Solution()
s = "-1 3 2 -1 -2 3 0 -2 0"
A = s.split(' ')
A = [int(i) for i in A]
print(solution.maxProduct(A))
