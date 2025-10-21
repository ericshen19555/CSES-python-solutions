def main():
    from sys import stdin
    e = stdin.readline

    def dinic(n: int, edges: list, s: int, t: int):
        from collections import deque
        from heapq import heappush, heappop

        inf = 10**20
        m = len(edges) << 1

        def spfa():
            q = deque([s])
            inq[s] = True
            h[s] = 0
            while q:
                i = q.popleft()
                inq[i] = False
                for j, ei in G[i]:
                    if flow[ei] == cap[ei]: continue
                    nv = h[i] + cost[ei]
                    if nv >= h[j]: continue
                    h[j] = nv
                    if not inq[j]:
                        inq[j] = True
                        q.append(j)

        def dijkstra():
            q = [(0, s)]
            dis = [inf] * n
            dis[s] = 0
            while q:
                v, i = heappop(q)
                if v > dis[i]: continue
                for j, ei in G[i]:
                    if flow[ei] == cap[ei]: continue
                    nv = v + cost[ei] + h[i] - h[j]
                    if nv >= dis[j]: continue
                    dis[j] = nv
                    heappush(q, (nv, j))
            for i in range(n):
                h[i] += dis[i]
            return dis[t] < inf

        def dfs(i, limit):
            nonlocal min_cost
            if i == t:
                return limit
            inq[i] = True
            sum_flow = 0
            for j, ei in G[i]:
                if inq[j]: continue
                if flow[ei] == cap[ei]: continue
                edge_cost = cost[ei]
                if h[j] != h[i] + edge_cost: continue
                pushed = dfs(j, min(limit - sum_flow, cap[ei] - flow[ei]))
                min_cost += pushed * edge_cost
                sum_flow += pushed
                flow[ei] += pushed
                flow[ei ^ 1] -= pushed
                if sum_flow == limit: break
            inq[i] = False
            if not sum_flow:
                h[i] = inf
            return sum_flow

        flow = [0] * m
        cap = [0] * m
        cost = [0] * m
        G = [[] for _ in range(n)]
        for ei, (i, j, w, c) in enumerate(edges):
            ei <<= 1
            cap[ei] = w
            cost[ei] = c
            cost[ei | 1] = -c
            G[i].append((j, ei))
            G[j].append((i, ei | 1))

        h = [inf] * n
        inq = [False] * n
        spfa()

        max_flow = min_cost = 0
        while dijkstra():
            max_flow += dfs(s, inf)
        return max_flow, min_cost, G, flow

    n, m, k = map(int, e().split())
    es = []
    for _ in range(m):
        a, b = map(int, e().split())
        es.append((a - 1, b - 1, 1, 1))
    es.append((n - 1, n, k, 0))

    max_flow, min_cost, G, flow = dinic(n + 1, es, 0, n)
    if max_flow < k:
        print(-1)
        return
    print(min_cost)

    for i in range(n - 1):
        G[i] = iter(G[i])

    for i, ei in G[0]:
        if flow[ei] < 1: continue
        cur = [1]
        while i != n:
            cur.append(i + 1)
            i = next(j for j, ei in G[i] if flow[ei] >= 1)
        print(len(cur))
        print(*cur)
main()
