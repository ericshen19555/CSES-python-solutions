def main():
    from sys import stdin
    e = stdin.readline

    def dinic(n: int, edges: list, s: int, t: int):
        inf = float("INF")
        m = len(edges) << 1

        def dfs(i, limit):
            if i == t:
                return limit
            sum_flow = 0  # 此點以下的最大流
            for j, edge_idx in G[i]:
                if flow[edge_idx] == cap[edge_idx]: continue
                if depth[j] != depth[i] + 1: continue
                pushed = dfs(j, min(limit - sum_flow, cap[edge_idx] - flow[edge_idx]))
                sum_flow += pushed
                flow[edge_idx] += pushed
                flow[edge_idx ^ 1] -= pushed
                if sum_flow == limit: break
            if not sum_flow:  # 重要優化
                depth[i] = None
            return sum_flow

        flow = [0] * m
        cap = [0] * m
        G = [[] for _ in range(n)]
        for edge_idx, (i, j, w) in enumerate(edges):
            cap[edge_idx << 1] = w
            G[i].append((j, edge_idx << 1))
            G[j].append((i, edge_idx << 1 | 1))

        max_flow = 0
        while True:
            bfs = [s]
            depth = [None] * n
            depth[s] = 0
            step = 1
            while bfs:
                nxt = []
                for i in bfs:
                    for j, edge_idx in G[i]:
                        if depth[j] is not None: continue  # visited
                        if flow[edge_idx] == cap[edge_idx]: continue  # 此路徑流量已滿
                        depth[j] = step
                        if j == t: break  # 到終點，bfs 結束
                        nxt.append(j)
                    else:
                        continue  # 未到終點，繼續 bfs 下個節點
                    break  # 到終點，bfs 結束
                else:  # 未到終點，繼續 bfs 下一輪
                    bfs = nxt
                    step += 1
                    continue
                break  # 到終點，bfs 結束
            else:
                break  # 未到終點，結束 Dinic 演算法

            max_flow += dfs(s, inf)
        return G, flow, cap

    n, m = map(int, e().split())
    es = []
    for _ in range(m):
        a, b = map(int, e().split())
        a, b = a-1, b-1
        es.append((a, b, 1))
        es.append((b, a, 1))

    G, flow, cap = dinic(n, es, 0, n-1)
    vis = [False] * n
    vis[0] = True
    q = [0]
    for i in q:
        for j, ei in G[i]:
            if ei & 1: continue
            if flow[ei] == cap[ei]: continue
            if vis[j]: continue
            vis[j] = True
            q.append(j)
    ans = []
    for ei in range(m << 1):
        a, b, _ = es[ei]
        if vis[a] and not vis[b]:
            ans.append(f"{a + 1} {b + 1}")
    print(len(ans))
    print("\n".join(ans))
main()