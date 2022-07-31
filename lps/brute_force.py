class Solution:
    def lps(self, s: str) -> str:
        n = len(s)
        dp = [0]*n
        dp2 = [0]*n
        for i in range(1, n):
            j = 1
            k = 0
            # while s[i - j] and s[i + j]:
            while i - j >= 0 and i + j < n:
                if s[i-j] == s[i+j]:
                    dp[i] += 1
                j += 1

            while i - k >= 0 and i + 1 + k < n:
                if s[i-k] == s[i+1+k]:
                    dp2[i] += 1
                k += 1
        # return max(dp)
        # print(max(dp))

        _max = max(dp)
        _max_index = 0
        for i in range(n):
            if dp[i] == _max:
                _max_index = i
                break

        _max_radius = max(dp2)
        if _max_radius != 0:
            _max_radius_index = 0
            for i in range(n):
                if dp2[i] == _max_radius:
                    _max_radius_index = i
                    break

        if _max_index * 2 + 1 > _max_radius*2:
            result = s[_max_index - _max: _max_index + 1 + _max]
        else:
            result = s[_max_radius_index + 1 - _max_radius: _max_radius_index + _max_radius + 1]

        print(result)



solve = Solution()
solve.lps("abcdcab")
solve.lps("abcdcba")
solve.lps("abcd")
solve.lps("abaadcd")
solve.lps("workattech")
solve.lps("workattaieng")
