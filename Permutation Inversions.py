# Mahonian numbers - OEIS A008302
# f(0, 0) = 1
# f(n, k) = sum(f(n-1, i), i = k-(n-1) ~ k)

mod = 10**9 + 7

def main():
    from sys import stdin
    e = stdin.readline

    n, k = map(int, e().split())
    dp = [0] * (k + 2)
    dp[0] = 1
    for i in range(n):
        r = min(k, (i + 1) * i >> 1)
        for j in range(r):
            dp[j + 1] = (dp[j + 1] + dp[j]) % mod
        for j in range(r, i - 1, -1):
            dp[j] -= dp[j - i - 1]
    print(dp[k] % mod)
main()