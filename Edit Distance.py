def main():
    from sys import stdin
    e = stdin.readline

    a, b = e().rstrip(), e().rstrip()
    m, n = len(a), len(b)
    if m < n: a, b, m, n = b, a, n, m
    dp = list(range(1, n + 1))
    for i in range(m):
        le, ul = i + 1, i
        for j in range(n):
            up = dp[j]
            le = dp[j] = min(le + 1, up + 1, ul + (a[i] != b[j]))
            ul = up
    print(le)
main()