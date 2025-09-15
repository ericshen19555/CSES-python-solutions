def main():
    from itertools import accumulate
    mul = lambda a, b: a * b % mod
    mod = 10**9 + 7

    lim = 10**6 + 1
    fac = list(accumulate(range(1, lim), func=mul, initial=1))
    inv = list(accumulate(range(lim-1, 0, -1), func=mul, initial=pow(fac[-1], -1, mod)))[::-1]

    n = int(input())
    if n & 1: return print(0)
    n >>= 1

    s = input()
    ri = up = 0
    for c in s:
        if c == "(":
            ri += 1
            if ri > n:
                return print(0)
        else:
            up += 1
            if up > ri:
                return print(0)
    if ri == n: return print(1)

    def comb(n, m):
        return fac[n] * inv[n - m] * inv[m] % mod

    r = n * 2 - ri - up
    print((comb(r, n - ri) - comb(r, n - ri - 1)) % mod)
main()