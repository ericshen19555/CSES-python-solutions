def main():
    from sys import stdin
    e = stdin.readline
    inf = float("INF")
    r = 10**5 + 1

    def y(x, v):
        return v[0] * x + v[1]

    def add(v):
        o, s, t = 1, 0, r
        while True:
            mid = s + t >> 1
            if y(mid, v) > y(mid, tr[o]):
                tr[o], v = v, tr[o]
            if y(s, v) > y(s, tr[o]):
                o = o << 1 | 0
                t = mid
                continue
            if y(t - 1, v) > y(t - 1, tr[o]):
                o = o << 1 | 1
                s = mid
                continue
            break

    def query(x):
        res = -inf
        o, s, t = 1, 0, r
        while True:
            res = max(res, y(x, tr[o]))
            if s + 1 == t: break
            mid = s + t >> 1
            if x < mid:
                o = o << 1
                t = mid
            else:
                o = o << 1 | 1
                s = mid
        return res

    tr = [(0, -inf)] * (r << 2)

    ans = []
    for _ in range(int(e())):
        o, *oo = map(int, e().split())
        if o == 1:
            add(oo)
        else:
            ans.append(query(oo[0]))
    print("\n".join(map(str, ans)))
main()