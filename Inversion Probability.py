def main():
    from sys import stdin
    from fractions import Fraction
    e = stdin.readline

    n = int(e())
    ans = 0
    s = 0
    dp = [0] * 101
    for r in map(int, e().split()):
        x = Fraction(1, r)
        cur = s
        for i in range(1, r + 1):
            cur -= dp[i]
            ans += cur * x
            dp[i] += x
        s += 1
    print(f"{ans:.6f}")
main()