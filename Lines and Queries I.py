def main():
    from sys import stdin
    e = stdin.readline
    inf = float("INF")
    r = 10**5 + 1

    def y(x, v):
        return v[0] * x + v[1]

    def add(v):
        o, s, t = 1, 0, r
        while s + 1 < t:
            if v[0] > tr[o][0]: tr[o], v = v, tr[o]
            mid = s + t >> 1
            if y(mid, tr[o]) >= y(mid, v):
                o = o << 1
                t = mid
            else:
                tr[o], v = v, tr[o]
                o = o << 1 | 1
                s = mid
        if y(s, v) > y(s, tr[o]):
            tr[o] = v

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