def main():
    from sys import stdin
    e = stdin.readline

    n = int(e())
    G = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = map(int, e().split())
        a, b = a-1, b-1
        G[a].append(b)
        G[b].append(a)

    pa = [-1] * n
    mx = [0] * n
    q = [0]
    for i in q:
        p = pa[i]
        for j in G[i]:
            if j == p: continue
            pa[j] = i
            q.append(j)
    siz = [1] * n
    for i in reversed(q):
        if not i: continue
        s, p = siz[i], pa[i]
        siz[p] += s
        mx[p] = max(mx[p], s)

    print(next(i + 1 for i in range(n) if max(n - siz[i], mx[i]) << 1 <= n))
main()