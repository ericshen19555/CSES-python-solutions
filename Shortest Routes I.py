def main():
    from sys import stdin
    from heapq import heappush, heappop
    inf = float("INF")
    e = stdin.readline

    n, m = map(int, e().split())
    G = [[] for _ in range(n)]
    for _ in range(m):
        a, b, w = map(int, e().split())
        a, b = a-1, b-1
        G[a].append((b, w))

    dis = [inf] * n
    dis[0] = 0
    q = [(0, 0)]
    while q:
        v, i = heappop(q)
        if v > dis[i]: continue
        for j, nv in G[i]:
            nv += v
            if nv >= dis[j]: continue
            dis[j] = nv
            heappush(q, (nv, j))
    print(*dis)

main()