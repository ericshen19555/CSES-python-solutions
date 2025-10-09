def main():
    from sys import stdin
    e = stdin.readline

    def y(x, v):
        return v[0] * x + v[1]

    def add(qs, qt, v):
        stk = [(1, 0, r)]
        while stk:
            o, s, t = stk.pop()
            if qt <= s or  t <= qs: continue
            if qs <= s and t <= qt:
                vv = v
                while True:
                    mid = s + t >> 1
                    if y(mid, vv) > y(mid, tr[o]): tr[o], vv = vv, tr[o]
                    if y(s, vv) > y(s, tr[o]):
                        o = o << 1 | 0
                        t = mid
                        continue
                    if y(t - 1, vv) > y(t - 1, tr[o]):
                        o = o << 1 | 1
                        s = mid
                        continue
                    break
            else:
                mid = s + t >> 1
                stk.append((o << 1 | 0, s, mid))
                stk.append((o << 1 | 1, mid, t))

    def query(x):
        res = -1
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
    tr = [(0, -1)] * (r << 2)

    for _ in range(n):
        a, b, c, d = map(int, e().split())
        if a > c: a, b, c, d = c, d, a, b
        m = (d - b) // (c - a)
        k = -m * a + b
        add(a, c + 1, (m, k))
    print(*[query(x) for x in range(r)])
main()