def main():
    from sys import stdin
    e = stdin.readline

    n, q = map(int, e().split())
    l = list(map(int, e().split()))
    r = l.index(1)  # 以 coin 為根，則子樹中有 coin 即為重要點 (題目保證至少有 1 coin)
    G = [[] for _ in range(n)]
    pa = [0] * n
    deg = [0] * n
    deg[r] = 2
    for _ in range(n - 1):
        a, b = map(int, e().split())
        a, b = a - 1, b - 1
        G[a].append(b)
        G[b].append(a)
        pa[a] ^= b
        pa[b] ^= a
        deg[a] += 1
        deg[b] += 1

    qu = [0] * n
    x = n
    ch = [-1] * n
    siz = [1] * n
    for i in range(n):
        while deg[i] == 1:
            deg[i] = 0
            x -= 1
            qu[x] = i
            p = pa[i]
            l[p] |= l[i]  # 子樹內有 coin 則為重要點
            if ch[p] == -1 or siz[ch[p]] < siz[i]:
                ch[p] = i
            siz[p] += siz[i]
            pa[p] ^= i
            deg[p] -= 1
            i = p
    qu[0] = r

    # l[i]: i 離重要點的最近距離
    l = [0 if v else n for v in l]
    bfs = [i for i, v in enumerate(l) if v == 0]
    base = len(bfs) - 1 << 1  # 遍歷所有重要點並回到原位的距離
    for i in bfs:
        nv = l[i] + 1
        for j in G[i]:
            if nv < l[j]:
                l[j] = nv
                bfs.append(j)

    dfc = 0
    dfn = [0] * n
    mn = [0] * n  # mn[i]: i 所在重鏈上，l 的前綴 min
    zkw = [0] * (n << 1)  # zkw[dfn[i]]: l 的區間 min
    top = [-1] * n
    dep = [0] * n
    for t in qu:
        if ~top[t]: continue
        i = t
        x = n
        while ~i:
            top[i] = t
            dep[i] = dep[pa[i]] + 1
            dfn[i] = dfc
            mn[i] = x = min(x, l[i])
            zkw[dfc + n] = l[i]
            dfc += 1
            i = ch[i]
    for i in range(n - 1, 0, -1): zkw[i] = min(zkw[i << 1], zkw[i << 1 | 1])

    ans = []
    for _ in range(q):
        a, b = map(int, e().split())
        a, b = a - 1, b - 1
        # 2*key + 2*dis_to_key[a] + 2*dis_to_key[b] - dis[a][b] - 2*min(dis_to_key[a...b])
        res = base + (l[a] + l[b]) * 2 - dep[a] - dep[b]
        v = n
        while top[a] != top[b]:
            if dep[top[a]] < dep[top[b]]: a, b = b, a
            v = min(v, mn[a])
            a = pa[top[a]]
        if dep[a] < dep[b]: a, b = b, a
        s, t = n + dfn[b], n + dfn[a] + 1
        while s < t:
            if s & 1:
                v = min(v, zkw[s])
                s += 1
            if t & 1:
                t -= 1
                v = min(v, zkw[t])
            s >>= 1
            t >>= 1
        res += (dep[b] - v) * 2
        ans.append(res)
    print("\n".join(map(str, ans)))
main()