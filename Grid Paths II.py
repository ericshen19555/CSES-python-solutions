mod = 10**9 + 7

def main():
    from sys import stdin
    from itertools import accumulate
    mul = lambda a, b: a * b % mod
    e = stdin.readline

    r, k = map(int, e().split())
    r -= 1
    lim = r * 2 + 1
    fac = list(accumulate(range(1, lim), func=mul, initial=1))
    inv = list(accumulate(range(lim - 1, 0, -1), func=mul, initial=pow(fac[-1], -1, mod)))[::-1]
    path = lambda x, y: fac[x + y] * inv[x] * inv[y] % mod if x >= 0 and y >= 0 else 0

    l = [r << 20 | r]
    for _ in range(k):
        x, y = map(int, e().split())
        x, y = x - 1, y - 1
        l.append(x << 20 | y)
    l = sorted(set(l))
    l = [(x >> 20, x & 0xfffff) for x in l]
    n = len(l)

    dp = [0] * n
    for i in range(n):
        x, y = l[i]
        v = path(x, y)
        for j in range(i):
            px, py = l[j]
            v -= dp[j] * path(x - px, y - py)
        dp[i] = v % mod
    print(dp[-1])
main()
