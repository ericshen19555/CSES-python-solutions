def main():
    from sys import stdin
    mod = 10**9 + 7
    e = stdin.readline

    n, m = map(int, e().split())
    it = map(int, e().split())
    pv = next(it)
    if pv:
        dp = [0] * (m + 2)
        dp[pv] = 1
    else:
        dp = [1] * (m + 2)
        dp[0] = dp[m + 1] = 0
    for v in it:
        if v:
            if pv:
                if pv - 1 <= v <= pv + 1:
                    dp[v] = dp[pv]
                else:
                    print(0)
                    return
            else:
                dp[v] += dp[v - 1] + dp[v + 1]
        else:
            if pv:
                x = dp[pv]
                dp = [0] * (m + 2)
                dp[pv - 1] = dp[pv] = dp[pv + 1] = x
            else:
                ndp = [0] * (m + 2)
                for i in range(1, m + 1):
                    ndp[i] = (dp[i - 1] + dp[i] + dp[i + 1]) % mod
                dp = ndp
        dp[0] = dp[m + 1] = 0
        pv = v
    print((dp[pv] % mod if pv else sum(dp)) % mod)
main()