import sys
count = 0


def climb_stairs(n: int) -> int:
    """
    dp easy challenge
    """
    if n == 1:
        return 1
    if n == 2:
        return 2
    dp = [0]
    dp = dp*(n+1)
    dp[1] = 1
    dp[2] = 2
    if n > 2:
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
    return dp[n]


print(climb_stairs(int(sys.argv[1])))
