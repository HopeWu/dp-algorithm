class Solution:
    def lps(self, s: str) -> str:
        n = len(s)
        dp = [1]*n
        starts = [0]*n
        ends = [0]*n
        for i in range(1, n):
            _max = 0
            for j in range(0, i):
                k = 0
                while(s[j+k] == s[i-k] and j+k < i-k):
                    k += 1
                if s[j+k] == s[i-k]:
                    # got one
                    if j+k == i-k:
                        # odd length case
                        if _max < k*2+1:
                            _max = k*2+1
                            starts[i] = j
                            ends[i] = i
                    if j+k == i-k+1:
                        # even length case
                        if _max < k*2:
                            _max = k*2
                            starts[i] = j
                            ends[i] = i
            if _max > dp[i-1]:

                dp[i] = _max
            else:
                starts[i] = starts[i-1]
                ends[i] = ends[i-1]
                dp[i] = dp[i-1]
        print(dp[n-1])
        return s[starts[n-1]: ends[n-1]+1]


solve = Solution()
print(solve.lps("abcdcab"))
print(solve.lps("abcdcba"))
print(solve.lps("abcd"))
print(solve.lps("abaadcd"))
print(solve.lps("workattech"))
print(solve.lps("workattaieng"))
