def main():
    from sys import stdin
    e = stdin.readline

    n, q = map(int, e().split())
    l = list(map(int, e().split()))
    G = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = map(int, e().split())
        a, b = a-1, b-1
        G[a].append(b)
        G[b].append(a)

    bfs = [0]
    pa = [-1] * n
    dep = [0] * n
    for i in bfs:
        p = pa[i]
        d = dep[i]
        for j in G[i]:
            if j == p: continue
            pa[j] = i
            dep[j] = d + 1
            bfs.append(j)
    siz = [1] * n
    ch = [-1] * n
    for i in reversed(bfs):
        if not i: continue
        p = pa[i]
        s = siz[i]
        siz[p] += s
        if ch[p] == -1 or s > siz[ch[p]]:
            ch[p] = i
    top = list(range(n))
    stk = [0]
    dfn = [0] * n
    bit = [0] * (n + 1)
    t = 1
    while stk:
        i = stk.pop()
        dfn[i] = t
        bit[t] = l[i]
        t += 1
        p, c = pa[i], ch[i]
        if c == -1: continue
        top[c] = top[i]
        for j in G[i]:
            if j == p or j == c: continue
            stk.append(j)
        stk.append(c)
    for i in range(1, n):
        ii = i + (i & -i)
        if ii <= n:
            bit[ii] += bit[i]

    ans = []
    for _ in range(q):
        o, i, *v = map(int, e().split())
        i -= 1
        if o == 1:
            v = v[0]
            d = v - l[i]
            l[i] = v
            i = dfn[i]
            while i <= n:
                bit[i] += d
                i += i & -i
        else:
            res = 0
            while ~i:
                tt = top[i]
                s, t = dfn[tt] - 1, dfn[i]
                while t > s:
                    res += bit[t]
                    t &= t-1
                while s > t:
                    res -= bit[s]
                    s &= s-1
                i = pa[tt]
            ans.append(res)
    print("\n".join(map(str, ans)))
main()