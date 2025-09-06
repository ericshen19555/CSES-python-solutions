def main():
    from sys import stdin
    from heapq import heappop, heappush
    mod = 10**9 + 7
    inf = float("INF")
    e = stdin.readline

    n, m = map(int, e().split())
    G = [[] for _ in range(n)]
    for _ in range(m):
        a, b, w = map(int, e().split())
        a, b = a-1, b-1
        G[a].append((b, w))

    dis = [inf] * n
    cnt = [0] * n
    mn = [n] * n
    mx = [0] * n
    dis[0], cnt[0], mn[0], mx[0] = 0, 1, 0, 0
    q = [(0, 0)]
    while q:
        v, i = heappop(q)
        if v > dis[i]: continue
        c, mnmn, mxmx = cnt[i] % mod, mn[i] + 1, mx[i] + 1
        for j, nv in G[i]:
            nv += v
            if nv < dis[j]:
                dis[j], cnt[j] = nv, c
                mn[j], mx[j] = mnmn, mxmx
                heappush(q, (nv, j))
            elif nv == dis[j]:
                cnt[j] += c
                mn[j] = min(mn[j], mnmn)
                mx[j] = max(mx[j], mxmx)
    print(dis[-1], cnt[-1] % mod, mn[-1], mx[-1])
main()