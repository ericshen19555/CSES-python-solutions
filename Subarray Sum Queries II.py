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

    ans = []
    for _ in range(q):
        s, t = map(int, e().split())
        s, t = s + n-1, t + n
        res = d = p = 0
        while s < t:
            if s & 1:
                res = max(res, dp[s], d + le[s])
                d = max(d + sm[s], ri[s])
                s += 1
            if t & 1:
                t -= 1
                res = max(res, dp[t], ri[t] + p)
                p = max(sm[t] + p, le[t])
            s >>= 1
            t >>= 1
        res = max(res, d + p)
        ans.append(res)
    print("\n".join(map(str, ans)))
main()