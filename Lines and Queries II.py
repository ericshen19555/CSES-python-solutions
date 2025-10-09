def main():
    from sys import stdin
    e = stdin.readline
    inf = float("INF")
    r = 10**5 + 1

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
            m, k, s, t = oo
            add(s, t + 1, (m, k))
        else:
            res = query(oo[0])
            ans.append(res if res > -inf else "NO")
    print("\n".join(map(str, ans)))
main()