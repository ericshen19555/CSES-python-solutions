def main():
    from itertools import accumulate
    mul = lambda a, b: a * b % mod
    mod = 10**9 + 7

    lim = 10**6 + 1
    fac = list(accumulate(range(1, lim), func=mul, initial=1))
    inv = list(accumulate(range(lim-1, 0, -1), func=mul, initial=pow(fac[-1], -1, mod)))[::-1]

    n = int(input())
    print(0 if n & 1 else fac[n] * inv[n >> 1] * inv[n >> 1] * pow((n >> 1) + 1, -1, mod) % mod)
main()