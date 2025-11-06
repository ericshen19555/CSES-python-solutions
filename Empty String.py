from itertools import accumulate
mod = 10**9 + 7

def main():
    mul = lambda a, b: a * b % mod
    s = input()
    n = len(s)

    lim = n + 1
    fac = list(accumulate(range(1, lim), func=mul, initial=1))
    inv = list(accumulate(range(n, 0, -1), func=mul, initial=pow(fac[-1], -1, mod)))[::-1]
    C = lambda n, k: fac[n] * inv[k] * inv[n - k] % mod

    dp = [[0] * i + [1] for i in range(1, n + 1)]
    for r in range(1, n):
        for i in range(n - r):
            j = i + r
            x = 0
            for k in range(i + 1, j + 1):
                if s[i] == s[k]:
                    x += dp[k-1][i+1] * dp[j][k+1] * C(j - i + 1 >> 1, k - i + 1 >> 1) % mod
            dp[j][i] = x % mod
    print(dp[-1][0])
main()