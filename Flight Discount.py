def main():
    from sys import stdin
    from heapq import heappop, heappush
    e = stdin.readline

    n, m = map(int, e().split())
    G = [[] for _ in range(n)]
    for _ in range(m):
        a, b, w = map(int, e().split())
        a, b = a-1, b-1
        G[a].append((b, w))

    dis = [float("INF")] * (n * 2)
    dis[0] = 0
    q = [(0, 0)]
    while q:
        v, i = heappop(q)
        if v > dis[i]: continue
        for j, nv in G[i % n]:
            nv += v
            if i < n:
                if nv < dis[j]:
                    dis[j] = nv
                    heappush(q, (nv, j))
                nv = (nv + v) >> 1
                if nv < dis[n + j]:
                    dis[n + j] = nv
                    heappush(q, (nv, n + j))
            elif nv < dis[n + j]:
                dis[n + j] = nv
                heappush(q, (nv, n + j))
    print(dis[-1])
main()