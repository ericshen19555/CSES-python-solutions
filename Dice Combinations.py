def main():
    from sys import stdin
    mod = 10**9 + 7
    e = stdin.readline

    n = int(e())
    dp = [0] * (n+7)
    dp[0] = 1
    for i in range(n):
        v = dp[i]
        for d in range(1, 7):
            dp[i + d] = (dp[i + d] + v) % mod
    print(dp[n])
main()