from itertools import accumulate
mod = 10**9 + 7

def main():
    mul = lambda a, b: a * b % mod
    n, k = map(int, input().split())
    # sum((-1)^i * C(k, i) * (k-i)^n for i in 0~k)
    lim = k + 1
    fac = list(accumulate(range(1, lim), func=mul, initial=1))
    inv = list(accumulate(range(k, 0, -1), func=mul, initial=pow(fac[-1], -1, mod)))[::-1]
    C = lambda n, k: fac[n] * inv[k] * inv[n - k] % mod
    print(sum((-1 if i & 1 else 1) * C(k, i) * pow(k - i, n, mod) for i in range(lim)) % mod)
main()