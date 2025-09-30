def main():
    from sys import stdin
    e = stdin.readline

    n, k = map(int, e().split())
    l = list(map(int, e().split()))
    m = n - k + 1

    tr = [(0, 0)] * (m << 2)

    def y(x, v):
        return x * v[0] + v[1]

    def update(o, s, t, v):
        mid = s + t >> 1
        if y(mid, v) > y(mid, tr[o]):
            tr[o], v = v, tr[o]
        if y(s, v) > y(s, tr[o]):
            update(o << 1 | 0, s, mid, v)
        if y(t - 1, v) > y(t - 1, tr[o]):
            update(o << 1 | 1, mid, t, v)

    def modify(o, s, t, qs, qt, v):
        if qt <= s or t <= qs:
            return
        if qs <= s and t <= qt:
            update(o, s, t, v)
            return
        mid = s + t >> 1
        modify(o << 1 | 0, s, mid, qs, qt, v)
        modify(o << 1 | 1, mid, t, qs, qt, v)

    def query(x):
        res = 0
        o, s, t = 1, 0, m
        while True:
            res = max(res, y(x, tr[o]))
            if s + 1 == t: break
            mid = s + t >> 1
            if x < mid:
                o = o << 1 | 0
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
        modify(1, 0, m, 0, ss, (h, h * (w - ss)))
        modify(1, 0, m, ss, s, (0, h * w))
        # -h * (x - s) + h * w
        # -h * x + h * (w + s)
        modify(1, 0, m, s, m, (-h, h * (w + s)))

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
    print(*map(query, range(m)))
main()