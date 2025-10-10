def main():
    from sys import stdin
    e = stdin.readline

    n, k = map(int, e().split())
    l = list(map(int, e().split()))
    m = n - k + 1

    tr = [(0, 0)] * (m << 2)

    def y(x, v):
        return x * v[0] + v[1]

    def modify(qs, qt, v):
        stk = [(1, 0, m)]
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
                if qs < mid:
                    stk.append((o << 1 | 0, s, mid))
                if qt > mid:
                    stk.append((o << 1 | 1, mid, t))

    def query(x):
        res = 0
        o, s, t = 1, 0, m
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

    def add(s, t, h):
        w = min(t - s, k)
        ss = t - k
        if ss > s: s, ss = ss, s
        # h * (x - ss) + h * w
        # h * x + h * (w - ss)
        modify(0, ss, (h, h * (w - ss)))
        modify(ss, s, (0, h * w))
        # -h * (x - s) + h * w
        # -h * x + h * (w + s)
        modify(s, m, (-h, h * (w + s)))

    stk = []
    pi = -1
    for i, v in enumerate(l):
        while ~pi and l[pi] >= v:
            h = l[pi]
            le = (pi := stk.pop()) + 1
            add(le, i, h)
        stk.append(pi)
        pi = i
    while ~pi:
        h = l[pi]
        le = (pi := stk.pop()) + 1
        add(le, n, h)
    print(*[query(x) for x in range(m)])
main()