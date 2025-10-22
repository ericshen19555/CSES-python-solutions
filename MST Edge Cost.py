def main():
    from sys import stdin
    e = stdin.readline

    n, m = map(int, e().split())
    es, si = [], []
    for i in range(m):
        a, b, w = map(int, e().split())
        es.append((a - 1, b - 1))
        si.append(w << 20 | i)
    si.sort()

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

    on_mst = [False] * m
    dsu = [-1] * n
    pa = [0] * n
    deg = [0] * n
    deg[0] = 2
    l = [0] * n
    res = 0
    ans = [0] * m
    for x in si:
        w, i = x >> 20, x & 0xfffff
        ans[i] = w
        a, b = es[i]
        on_mst[i] = merge(a, b)
        if on_mst[i]:
            res += w
            pa[a] ^= b
            pa[b] ^= a
            deg[a] += 1
            deg[b] += 1
            l[a] ^= w
            l[b] ^= w
    siz = [1] * n
    ch = [-1] * n
    path = [0] * n
    idx = n
    for i in range(n):
        while deg[i] == 1:
            deg[i] = 0
            idx -= 1
            path[idx] = i
            p = pa[i]
            siz[p] += 1
            if ch[p] == -1 or siz[ch[p]] < siz[i]:
                ch[p] = i
            l[p] ^= l[i]
            pa[p] ^= i
            deg[p] -= 1
            i = p

    dfn = [0] * n
    zkw = [0] * (n << 1)
    top = [-1] * n
    dfnn = 0
    for i in path:
        if ~top[i]: continue
        t = i
        x = 0
        while ~i:
            dfn[i] = dfnn
            zkw[dfnn + n] = l[i]
            dfnn += 1
            x = l[i] = max(l[i], x)
            top[i] = t
            i = ch[i]
    for i in range(n - 1, 0, -1):
        zkw[i] = max(zkw[i << 1], zkw[i << 1 | 1])

    for ei in range(m):
        if on_mst[ei]:
            ans[ei] = res
            continue
        a, b = es[ei]
        w = 0
        while top[a] != top[b]:
            if dfn[top[a]] < dfn[top[b]]: a, b = b, a
            w = max(w, l[a])
            a = pa[top[a]]
        s, t = dfn[a] + n + 1, dfn[b] + n + 1
        if s > t: s, t = t, s
        while s < t:
            if s & 1:
                w = max(w, zkw[s])
                s += 1
            if t & 1:
                t -= 1
                w = max(w, zkw[t])
            s >>= 1
            t >>= 1
        ans[ei] += res - w
    print(*ans, sep="\n")
main()