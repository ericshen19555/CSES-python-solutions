def main():
    from sys import stdin
    from operator import itemgetter
    e = stdin.readline

    m, n = map(int, e().split())
    a = list(map(int, e().split()))[::-1]
    b = list(map(int, e().split()))[::-1]
    if m < n: a, b, m, n = b, a, n, m
    dp = [[(0, None)] * (n + 1) for _ in range(m + 1)]
    best = (0, None)
    for i in range(m):
        for j in range(n):
            if a[i] == b[j]:
                dp[i][j] = (dp[i - 1][j - 1][0] + 1, (i, j))
                best = max(best, dp[i][j], key=itemgetter(0))
            else:
                dp[i][j] = max(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j], key=itemgetter(0))
    print(best[0])
    best = best[1]
    while best is not None:
        print(a[best[0]], end=" ")
        best = dp[best[0] - 1][best[1] - 1][1]
main()