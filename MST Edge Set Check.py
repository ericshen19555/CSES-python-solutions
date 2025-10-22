def main():
    from sys import stdin
    e = stdin.readline

    n, m, q = map(int, e().split())
    es, ws = [], []
    for i in range(m):
        a, b, w = map(int, e().split())
        es.append((a - 1, b - 1))
        ws.append(w)
    o = sorted(range(m), key=ws.__getitem__)
    mp = {v: i for i, v in enumerate(ws[i] for i in o)}

    qs = [[] for _ in range(m)]
    for gi in range(q):
        e()
        for ei in map(int, e().split()):
            ei -= 1
            qq = qs[mp[ws[ei]]]
            if not qq or (gg := qq[-1])[0] != gi:
                qq.append(gg := (gi, []))
            gg[1].append(ei)

    def find(x):
        if dsu[x] < 0:
            return x
        dsu[x] = find(dsu[x])
        return dsu[x]

    def merge(a, b):
        a, b = find(a), find(b)
        if a == b: return False
        if dsu[a] == dsu[b]: dsu[a] -= 1
        elif dsu[a] > dsu[b]: a, b = b, a
        dsu[b] = a
        return True

    ans = ["YES"] * q
    j, pw = -1, 0
    dsu = [-1] * n
    temp = [0] * n
    for i in range(m):
        w, qq = ws[o[i]], qs[i]
        if pw != w:
            if ~j:
                for k in range(j, i):
                    merge(*es[o[k]])
            j, pw = i, w
        for qi, g in qq:
            if ans[qi] == "NO": continue
            for ei in g:
                a, b = es[ei]
                ra, rb = find(a), find(b)
                temp[a] = ra
                temp[b] = rb
                temp[ra] = dsu[ra]
                temp[rb] = dsu[rb]
            dsu, temp = temp, dsu
            if not all(merge(*es[ei]) for ei in g):
                ans[qi] = "NO"
            dsu, temp = temp, dsu
    print("\n".join(ans))
main()