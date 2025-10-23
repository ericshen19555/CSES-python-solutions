def main():
    from sys import stdin
    from heapq import heappush, heappop
    e = stdin.readline
    inf = float("INF")

    n, m = map(int, e().split())
    l = list(map(int, e().split()))
    dis = [inf] * (n + m)
    dis[0] = 0
    G = [[] for _ in range(n + m)]
    for g in range(n, n + m):
        e()
        G_g = G[g]
        for i in map(int, e().split()):
            i -= 1
            G[i].append(g)
            G_g.append(i)

    h = [(0, 0)]
    while h:
        v, i = heappop(h)
        if v > dis[i]: continue
        for j in G[i]:
            nv = v + (l[j - n] if j >= n else 0)
            if nv >= dis[j]: continue
            dis[j] = nv
            heappush(h, (nv, j))
    print(*dis[:n])
main()