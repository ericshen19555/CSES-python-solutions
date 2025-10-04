def main():
    from sys import stdin
    e = stdin.readline
    inf = float("INF")
    m = 10**6 + 1

    n, p0 = map(int, e().split())
    l = list(map(int, e().split()))
    p = list(map(int, e().split()))

    tr = [(0, inf)] * (m << 2)

    def y(x, v):
        return v[0] * x + v[1]

    def add(v):
        o, s, t = 1, 0, m
        while s + 1 < t:
            mid = s + t >> 1
            if v[0] < tr[o][0]:
                tr[o], v = v, tr[o]
            if y(mid, v) >= y(mid, tr[o]):
                o = o << 1 | 0
                t = mid
            else:
                tr[o], v = v, tr[o]
                o = o << 1 | 1
                s = mid
        if y(s, v) < y(s, tr[o]):
            tr[o] = v

    def query(x):
        res = inf
        o, s, t = 1, 0, m
        while True:
            res = min(res, y(x, tr[o]))
            if s + 1 == t: break
            mid = s + t >> 1
            if x < mid:
                o = o << 1 | 0
                t = mid
            else:
                o = o << 1 | 1
                s = mid
        return res

    add((p0, 0))
    for i in range(n):
        ans = query(l[i])
        add((p[i], ans))
    print(ans)
main()