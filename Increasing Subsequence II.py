def main():
    from sys import stdin
    mod = 10**9 + 7
    e = stdin.readline

    n = int(e())
    l = list(map(int, e().split()))
    sl = sorted(range(n-1, -1, -1), key=l.__getitem__)

    ans = 0
    bit = [0] * (n + 1)
    for i in sl:
        res = 1
        ii = i
        while ii:
            res += bit[ii]
            ii &= ii-1
        res %= mod
        ans += res
        ii = i + 1
        while ii <= n:
            bit[ii] += res
            ii += ii & -ii
    print(ans % mod)
main()