def main():
    from sys import stdin
    e = stdin.readline

    n, q = map(int, e().split())
    l = list(map(int, e().split()))

    qs = [[] for _ in range(n)]
    for qi in range(q):
        s, t = map(int, e().split())
        qs[s - 1].append((t, qi))

    stk = []
    pi, pv = n, float("INF")
    bit = [0] * (n + 1)
    ans = [0] * q
    for i in range(n-1, -1, -1):
        v = l[i]
        while pv <= v:
            x = pi + 1
            while x <= n:
                bit[x] -= 1
                x += x & -x
            pi, pv = stk.pop()
        stk.append((pi, pv))
        pi, pv = i, v
        x = i + 1
        while x <= n:
            bit[x] += 1
            x += x & -x
        for t, qi in qs[i]:
            res = 0
            s = i
            while t > s:
                res += bit[t]
                t &= t-1
            while s > t:
                res -= bit[s]
                s &= s-1
            ans[qi] = res
    print("\n".join(map(str, ans)))
main()