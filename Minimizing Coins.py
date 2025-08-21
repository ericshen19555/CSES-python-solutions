def main():
    from sys import stdin
    inf = 10**6 + 1
    e = stdin.readline

    n, m = map(int, e().split())
    lim = m + 1
    dp = [inf] * lim
    dp[0] = 0
    for v in map(int, e().split()):
        if v >= lim: continue
        for i in range(v, lim):
            if dp[i - v] < dp[i]: dp[i] = dp[i - v] + 1
    print(-1 if dp[m] is inf else dp[m])
main()