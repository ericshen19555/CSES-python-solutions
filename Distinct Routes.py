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
        return max_flow, flow

    n, m = map(int, e().split())
    es = []
    for _ in range(m):
        a, b = map(int, e().split())
        a, b = a-1, b-1
        es.append((a, b, 1))

    max_flow, flow = dinic(n, es, 0, n-1)

    G = [[] for _ in range(n)]
    for ei in range(m):
        a, b, _ = es[ei]
        if flow[ei << 1] == 1:
            G[a].append(b)

    ans = [str(max_flow)]
    while G[0]:
        cur = [1]
        i = G[0].pop()
        while i != n-1:
            cur.append(i + 1)
            i = G[i].pop()
        cur.append(n)
        ans.append(f"{len(cur)}\n"
                   f"{' '.join(map(str, cur))}")
    print("\n".join(ans))
main()