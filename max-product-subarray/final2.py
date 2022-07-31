class Solution:
    def maxProduct(self, A: [int]) -> int:
        _max = A[0]
        _min = A[0]
        _max_so_far = A[0]
        skip_flag = 1
        for i in A:
            if skip_flag == 1:
                skip_flag = 0
                continue
            tmp = _max
            _max = max(i, i*_max, i*_min)
            _min = min(i, i*tmp, i*_min)
            _max_so_far = max(_max_so_far, _max)

        return _max_so_far


solution = Solution()
s = "-1 3 2 -1 -2 3 0 -2"
A = s.split(' ')
A = [int(i) for i in A]
print(solution.maxProduct(A))
