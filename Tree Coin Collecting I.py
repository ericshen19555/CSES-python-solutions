def main():
    from sys import stdin
    e = stdin.readline

    n, q = map(int, e().split())
    qu = [i for i, v in enumerate(map(int, e().split())) if v]
    G = [[] for _ in range(n)]
    pa = [0] * n
    deg = [0] * n
    deg[0] = 2
    for _ in range(n - 1):
        a, b = map(int, e().split())
        a, b = a - 1, b - 1
        G[a].append(b)
        G[b].append(a)
        pa[a] ^= b
        pa[b] ^= a
        deg[a] += 1
        deg[b] += 1

    dis = [n] * n
    for i in qu: dis[i] = 0
    for i in qu:
        for j in G[i]:
            if dis[j] < n: continue
            dis[j] = dis[i] + 1
            qu.append(j)

    x = n
    ch = [-1] * n
    siz = [1] * n
    for i in range(n):
        while deg[i] == 1:
            deg[i] = 0
            x -= 1
            qu[x] = i
            p = pa[i]
            if ch[p] == -1 or siz[ch[p]] < siz[i]:
                ch[p] = i
            siz[p] += siz[i]
            pa[p] ^= i
            deg[p] -= 1
            i = p
    x = qu[0] = 0
    dfn = deg  # reuse
    top = [-1] * n
    zkw = [0] * (n << 1)
    dep = [-1] * n
    for i in qu:
        if ~top[i]: continue
        t = i
        v = dis[i]
        while ~i:
            dfn[i] = x
            zkw[x + n] = dis[i]
            x += 1
            top[i] = t
            dep[i] = dep[pa[i]] + 1
            v = dis[i] = min(dis[i], v)
            i = ch[i]
    for i in range(n - 1, 0, -1):
        zkw[i] = min(zkw[i << 1], zkw[i << 1 | 1])

    ans = []
    for _ in range(q):
        a, b = map(int, e().split())
        a, b = a - 1, b - 1
        mn = n
        res = dep[a] + dep[b]
        while top[a] != top[b]:
            if dep[top[a]] < dep[top[b]]: a, b = b, a
            mn = min(mn, dis[a])
            a = pa[top[a]]
        if dep[a] < dep[b]: a, b = b, a
        res -= dep[b] << 1
        s, t = dfn[b] + n, dfn[a] + n + 1
        while s < t:
            if s & 1:
                mn = min(mn, zkw[s])
                s += 1
            if t & 1:
                t -= 1
                mn = min(mn, zkw[t])
            s >>= 1
            t >>= 1
        res += mn << 1
        ans.append(res)
    print(*ans, sep="\n")
main()