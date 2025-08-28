def main():
    from sys import stdin
    e = stdin.readline

    m, n = map(int, e().split())
    mx = max(m, n)
    dp = [[0] * (mx + 1) for _ in range(mx + 1)]
    for i in range(1, mx + 1):
        row = dp[i]
        for j in range(1, i):
            col = dp[j]
            x = i * j
            for k in range(1, (i >> 1) + 1):
                x = min(x, col[k] + col[i - k])
            for k in range(1, (j >> 1) + 1):
                x = min(x, row[k] + row[j - k])
            row[j] = col[i] = x + 1
    print(dp[m][n])
main()
