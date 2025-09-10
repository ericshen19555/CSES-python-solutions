def main():
    from sys import stdin
    e = stdin.readline
    m = 10**6 + 1
    bl = m.bit_length()
    max = lambda a, b: a if a >= b else b

    n, q = map(int, e().split())
    dp = [[0] * m for _ in range(bl)]
    cur = dp[0]
    for _ in range(n):
        s, t = map(int, e().split())
        cur[t] = max(cur[t], s)
    le = 0
    for i in range(1, m):
        le = cur[i] = max(cur[i], le)
    pre = cur
    for k in range(1, bl):
        if not pre[-1]:
            bl = k
            break
        cur = dp[k]
        le = 0
        for i in range(1, m):
            le = cur[i] = max(le, pre[pre[i]])
        pre = cur
    ans = []
    for _ in range(q):
        s, t = map(int, e().split())
        res = 0
        for k in range(bl-1, -1, -1):
            if dp[k][t] >= s:
                t = dp[k][t]
                res |= 1 << k
        ans.append(res)
    print("\n".join(map(str, ans)))
main()