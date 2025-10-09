def main():
    from sys import stdin
    e = stdin.readline

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
        res = 0
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

    n, m = map(int, e().split())
    r = m + 1
    tr = [(0, 0)] * (r << 2)

    for _ in range(n):
        a, b = map(int, e().split())
        v = ((b - a) // m, a)
        add(v)
    print(*[query(x) for x in range(r)])
main()