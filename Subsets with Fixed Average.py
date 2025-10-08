mod = 10 ** 9 + 7

def main():
    from sys import stdin
    e = stdin.readline

    n, a = map(int, e().split())
    l = [int(v) - a for v in e().split()]
    lo = sum(v for v in l if v < 0)
    hi = sum(v for v in l if v > 0) + 1

    dp = [0] * (hi - lo)
    dp[0] = 1
    for v in l:
        for i in reversed(range(lo + v, hi)) if v >= 0 else range(lo, hi + v):
            dp[i] = (dp[i] + dp[i - v]) % mod
    print((dp[0] - 1) % mod)
main()