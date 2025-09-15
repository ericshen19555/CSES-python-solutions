def main():
    from sys import stdin
    from itertools import accumulate
    mul = lambda a, b: a * b % mod
    mod = 10**9 + 7
    e = stdin.readline

    lim = 2 * 10**6 + 1
    fac = list(accumulate(range(1, lim), func=mul, initial=1))
    inv = list(accumulate(range(lim-1, 0, -1), func=mul, initial=pow(fac[-1], -1, mod)))[::-1]

    n, m = map(int, e().split())
    # H(n, m) = C(n + m - 1, m)
    print(fac[n + m - 1] * inv[n - 1] * inv[m] % mod)
main()