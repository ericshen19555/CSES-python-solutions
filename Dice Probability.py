def main():
    from sys import stdin
    e = stdin.readline

    n, lo, hi = map(int, e().split())
    m = n * 6
    dp = [1] + [0] * m
    for r in range(n):
        for i in range(m, -1, -1):
            dp[i] = sum(dp[max(0, i - 6):i]) / 6
    print(f"{sum(dp[lo:hi+1]):.6f}")
main()