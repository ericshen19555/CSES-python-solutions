def main():
    mod = 10**9 + 7
    n = int(input())

    if n & 3 and (n + 1) & 3:
        return print(0)

    t = n * (n + 1) >> 2
    lim = t + 1
    dp = [0] * lim
    dp[~0] = 1
    for v in range(1, n+1):
        for i in range(lim - v):
            dp[i] = (dp[i] + dp[i + v]) % mod
    print(dp[0] * pow(2, -1, mod) % mod)
main()