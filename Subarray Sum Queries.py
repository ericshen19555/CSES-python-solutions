def main():
    from sys import stdin
    e = stdin.readline

    def merge(i: int) -> None:
        sm[i] = sm[i << 1] + sm[i << 1 | 1]
        le[i] = max(le[i << 1], sm[i << 1] + le[i << 1 | 1])
        ri[i] = max(ri[i << 1] + sm[i << 1 | 1], ri[i << 1 | 1])
        dp[i] = max(dp[i << 1], dp[i << 1 | 1], ri[i << 1] + le[i << 1 | 1])

    n, q = map(int, e().split())
    l = list(map(int, e().split()))
    sm = [0] * n + l
    le = [0] * n + l
    ri = [0] * n + l
    dp = [0] * n + l
    for i in range(n-1, 0, -1):
        merge(i)

    ql, qr = [], []
    s, t = n, n << 1
    while s < t:
        if s & 1:
            ql.append(s)
            s += 1
        if t & 1:
            t -= 1
            qr.append(t)
        s >>= 1
        t >>= 1

    ans = []
    for _ in range(q):
        i, v = map(int, e().split())
        i += n-1
        sm[i] = le[i] = ri[i] = dp[i] = v
        while i > 1:
            i >>= 1
            merge(i)
        res = d = p = 0
        for i in ql:
            res = max(res, dp[i], d + le[i])
            d = max(d + sm[i], ri[i])
        for i in qr:
            res = max(res, dp[i], ri[i] + p)
            p = max(sm[i] + p, le[i])
        res = max(res, d + p)
        ans.append(res)
    print("\n".join(map(str, ans)))
main()