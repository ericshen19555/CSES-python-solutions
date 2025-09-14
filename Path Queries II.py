def main():
    from sys import stdin
    e = stdin.readline

    n, q = map(int, e().split())
    l = list(map(int, e().split()))
    pa = [0] * n
    deg = [0] * n
    deg[0] = 2
    for _ in range(n - 1):
        a, b = map(int, e().split())
        a, b = a - 1, b - 1
        pa[a] ^= b
        pa[b] ^= a
        deg[a] += 1
        deg[b] += 1

    siz = [1] * n
    ch = [-1] * n
    top_down = [0] * n
    idx = n
    for i in range(n):
        while deg[i] == 1:
            deg[i] = -1
            idx -= 1
            top_down[idx] = i
            p = pa[i]
            s = siz[i]
            siz[p] += s
            if ch[p] == -1 or s > siz[ch[p]]:
                ch[p] = i
            pa[p] ^= i
            deg[p] -= 1
            i = p

    top = [-1] * n
    dfn = [-1] * n
    zkw = [0] * (n << 1)
    t = 0
    for i in top_down:
        if dfn[i] != -1: continue
        tt = i
        while i != -1:
            top[i] = tt
            zkw[t + n] = l[i]
            dfn[i] = t
            t += 1
            i = ch[i]
    for i in range(n - 1, 0, -1):
        zkw[i] = max(zkw[i << 1], zkw[i << 1 | 1])

    def query(s, t):
        res = 0
        s, t = s + n, t + n
        while s < t:
            if s & 1:
                res = max(res, zkw[s])
                s += 1
            if t & 1:
                t -= 1
                res = max(res, zkw[t])
            s >>= 1
            t >>= 1
        return res

    ans = []
    for _ in range(q):
        o, a, b = map(int, e().split())
        if o == 1:
            i, v = a - 1, b
            i = dfn[i] + n
            zkw[i] = v
            while i > 1:
                i >>= 1
                zkw[i] = max(zkw[i << 1], zkw[i << 1 | 1])
        else:
            res = 0
            a, b = a - 1, b - 1
            while top[a] != top[b]:
                if dfn[top[a]] < dfn[top[b]]: a, b = b, a
                res = max(res, query(dfn[top[a]], dfn[a] + 1))
                a = pa[top[a]]
            if dfn[a] < dfn[b]: a, b = b, a
            res = max(res, query(dfn[b], dfn[a] + 1))
            ans.append(res)
    print("\n".join(map(str, ans)))
main()