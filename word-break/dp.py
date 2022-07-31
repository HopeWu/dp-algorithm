class Solution:
    def wordBreak(self, s: str, w: [str]) -> bool:
        n = len(s)
        dp = [0]*n
        for i in range(n):
            for word in w:
                wl = len(word)
                if wl < i+1:
                    if s[i+1-wl:i+1] == word:
                        if dp[i-wl] == 1:
                            dp[i] = 1
                            break
                if wl == i+1:
                    if s[:i+1] == word:
                        dp[i] = 1
                        break

        return bool(dp[n-1])


sl = Solution()
s = 'workattech'
s = 'roundandround'
w = ['tech', 'work', 'problem', 'at']
w = ['and', 'round']
print(sl.wordBreak(s, w))


