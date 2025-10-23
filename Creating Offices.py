def main():
    from sys import stdin
    e = stdin.readline

    n, k = map(int, e().split())
    h = n.bit_length()
    G = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = map(int, e().split())
        a, b = a - 1, b - 1
        G[a].append(b)
        G[b].append(a)
    cd = [n] * n + [-1]
    cp = [0] * n
    siz = [0] * (n + 1)
    pa = [-1] * n

    rec = [0]
    dis = [[-1] * n for _ in range(h)]
    for r in rec:
        cpc = pa[r]
        d = cd[cpc] + 1
        q = [r]
        pa[r] = -1
        siz[r] = 1
        for i in q:
            p = pa[i]
            for j in G[i]:
                if j == p or cd[j] < d: continue
                siz[j] = 1
                pa[j] = i
                q.append(j)
        for i in reversed(q):
            siz[pa[i]] += siz[i]
        half = siz[r] >> 1
        i = r
        while True:
            p = pa[i]
            for j in G[i]:
                if j == p or cd[j] < d: continue
                if siz[j] > half:
                    i = j
                    break
            else:
                c = i
                break
        cp[c] = cpc
        cd[c] = d
        dis_d = dis[d]
        dis_d[c] = 0
        q = [c]
        for i in q:
            v = dis_d[i]
            for j in G[i]:
                if cd[j] < d or ~dis_d[j]: continue
                dis_d[j] = v + 1
                q.append(j)
        for j in G[c]:
            if cd[j] < d: continue
            pa[j] = c
            rec.append(j)

    q = [0]
    for i in q:
        p = pa[i]
        for j in G[i]:
            if j == p: continue
            pa[j] = i
            q.append(j)

    ans = []
    mn = [k] * n
    for i in reversed(q):
        c, d = i, cd[i]
        for d in range(cd[i], -1, -1):
            if dis[d][i] + mn[c] < k:
                break
            c = cp[c]
        else:
            ans.append(i + 1)
            c, d = i, cd[i]
            for d in range(cd[i], -1, -1):
                mn[c] = min(mn[c], dis[d][i])
                c = cp[c]
    print(len(ans))
    print(*ans)
main()