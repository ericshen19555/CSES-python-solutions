def main():
    from sys import stdin
    from itertools import accumulate
    mul = lambda a, b: a * b % mod
    mod = 10**9 + 7
    e = stdin.readline

    lim = 10**6 + 1
    fac = list(accumulate(range(1, lim), func=mul, initial=1))
    inv = list(accumulate(range(lim-1, 0, -1), func=mul, initial=pow(fac[-1], -1, mod)))[::-1]

    ans = []
    for _ in range(int(e())):
        n, m = map(int, e().split())
        ans.append(fac[n] * inv[m] * inv[n - m] % mod)
    print("\n".join(map(str, ans)))
main()