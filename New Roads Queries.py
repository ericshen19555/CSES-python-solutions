def main():
    from sys import stdin
    from bisect import bisect_left
    e = stdin.readline
    VAL = LE = 0
    RI = 1

    def build(s, t):
        if s + 1 == t:
            return [-1]
        mid = s + t >> 1
        return [build(s, mid), build(mid, t)]

    def modify(o, s, t, i, v):
        o = o.copy()
        if s + 1 == t:
            o[VAL] = v
        else:
            mid = s + t >> 1
            if i < mid:
                o[LE] = modify(o[LE], s, mid, i, v)
            else:
                o[RI] = modify(o[RI], mid, t, i, v)
        return o

    def query(o, i):
        s, t = 0, m
        while s + 1 < t:
            mid = s + t >> 1
            if i < mid:
                o = o[LE]
                t = mid
            else:
                o = o[RI]
                s = mid
        return o[VAL]

    def find(o, x):
        p = query(o, x)
        if p < 0: return o, x
        o, p = find(o, p)
        o = modify(o, 0, m, x, p)
        return o, p

    def merge(o, a, b):
        o, a = find(o, a)
        o, b = find(o, b)
        if a != b:
            ra, rb = query(o, a), query(o, b)
            if ra == rb: o = modify(o, 0, m, a, ra - 1)
            elif ra > rb: a, b = b, a
            o = modify(o, 0, m, b, a)
        return o

    n, m, q = map(int, e().split())
    m += 1
    os = [o := build(0, m)]
    for i in range(1, m):
        a, b = map(int, e().split())
        a, b = a-1, b-1
        o = merge(o, a, b)
        os.append(o)
    ans = []

    def check(x):
        os[x], aa = find(os[x], a)
        os[x], bb = find(os[x], b)
        return aa == bb

    for _ in range(q):
        a, b = map(int, e().split())
        a, b = a-1, b-1
        if find(o, a) != find(o, b):
            ans.append(-1)
            continue
        ans.append(bisect_left(range(m), True, key=check))
    print(*ans, sep="\n")
main()