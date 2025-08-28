def main():
    from sys import stdin
    e = stdin.readline

    n = int(e())
    dp = [[0] * i for i in range(1, n + 1)]
    l = list(map(int, e().split()))
    if n & 1:
        for i, v in enumerate(l):
            dp[i][i] = v

    for r in range(1, n):
        if (n ^ r) & 1:
            for i in range(n - r):
                j = i + r
                dp[j][i] = max(dp[j][i + 1] + l[i], dp[j - 1][i] + l[j])
        else:
            for i in range(n - r):
                j = i + r
                dp[j][i] = min(dp[j][i + 1], dp[j - 1][i])
    print(dp[-1][0])
main()