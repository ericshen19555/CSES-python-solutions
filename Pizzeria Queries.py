def main():
    from sys import stdin
    e = stdin.readline

    n, q = map(int, e().split())
    l = list(map(int, e().split()))
    le = [0] * n
    ri = [0] * n
    le += (l[i] - i for i in range(n))
    ri += (l[i] + i for i in range(n))
    for i in range(n-1, 0, -1):
        le[i] = min(le[i << 1], le[i << 1 | 1])
        ri[i] = min(ri[i << 1], ri[i << 1 | 1])

    ans = []
    for _ in range(q):
        o: str = e()
        if o.startswith("1"):
            p, v = map(int, o.split()[1:])
            p -= 1
            i = p + n
            le[i] = v - p
            ri[i] = v + p
            while i > 1:
                i >>= 1
                le[i] = min(le[i << 1], le[i << 1 | 1])
                ri[i] = min(ri[i << 1], ri[i << 1 | 1])
        else:
            p = int(o.split()[1]) - 1
            lele = riri = float("INF")
            s, t = n, p + n
            while s < t:
                if s & 1:
                    lele = min(lele, le[s])
                    s += 1
                if t & 1:
                    t -= 1
                    lele = min(lele, le[t])
                s >>= 1
                t >>= 1
            s, t = p + n, n << 1
            while s < t:
                if s & 1:
                    riri = min(riri, ri[s])
                    s += 1
                if t & 1:
                    t -= 1
                    riri = min(riri, ri[t])
                s >>= 1
                t >>= 1
            ans.append(min(lele + p, riri - p))
    print("\n".join(map(str, ans)))
main()