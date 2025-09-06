def main():
    from sys import stdin
    from heapq import heappop, heappush
    inf = float("INF")
    e = stdin.readline

    n, m, k = map(int, e().split())
    G = [[] for _ in range(n)]
    R = [[] for _ in range(n)]
    for _ in range(m):
        a, b, w = map(int, e().split())
        a, b = a-1, b-1
        G[a].append((b, w))
        R[b].append((a, w))

    # Dijkstra from t
    dis = [inf] * n
    dis[-1] = 0
    q = [(0, n-1)]
    while q:
        v, i = heappop(q)
        if v > dis[i]: continue
        for j, nv in R[i]:
            nv += v
            if nv < dis[j]:
                dis[j] = nv
                heappush(q, (nv, j))

    # A* from s to t
    ans = [inf] * k
    cnt = [0] * n
    q = [(dis[0], 0)]
    while q:
        v, i = heappop(q)
        v -= dis[i]
        if i == n-1: ans[cnt[i]] = v
        cnt[i] += 1
        if cnt[n-1] >= k: break
        if cnt[i] > k: continue
        for j, w in G[i]:
            heappush(q, (v + w + dis[j], j))
    print(*ans)
main()