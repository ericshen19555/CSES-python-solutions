def main():
    from sys import stdin
    from itertools import accumulate
    inf = float("INF")
    e = stdin.readline

    n = int(e())
    l = list(accumulate(map(int, e().split()), initial=0))

    dp = [[0] * i for i in range(n + 1)]
    best = [[i - 1] * i for i in range(n + 1)]
    for r in range(2, n + 1):
        for i in range(n - r + 1):
            j = i + r
            dp[j][i] = inf
            for k in range(best[j - 1][i], best[j][i + 1] + 1):
                if k == i: continue
                x = dp[k][i] + dp[j][k]
                if x < dp[j][i]:
                    dp[j][i] = x
                    best[j][i] = k
            dp[j][i] += l[j] - l[i]
    print(dp[n][0])
main()