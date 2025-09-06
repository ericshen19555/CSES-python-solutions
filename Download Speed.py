def main():
    from sys import stdin
    e = stdin.readline

    def dinic(n: int, edges: list, s: int, t: int) -> int:
        inf = float("INF")
        m = len(edges) << 1

        def dfs(i, limit):
            if i == t:
                return limit
            sum_flow = 0  # 此點以下的最大流
            for j, ei in G[i]:
                if flow[ei] == cap[ei]: continue
                if depth[j] != depth[i] + 1: continue
                pushed = dfs(j, min(limit - sum_flow, cap[ei] - flow[ei]))
                sum_flow += pushed
                flow[ei] += pushed
                flow[ei ^ 1] -= pushed
                if sum_flow == limit: break
            if not sum_flow:  # 重要優化
                depth[i] = None
            return sum_flow

        flow = [0] * m
        cap = [0] * m
        G = [[] for _ in range(n)]
        for ei, (i, j, w) in enumerate(edges):
            cap[ei << 1] = w
            G[i].append((j, ei << 1))
            G[j].append((i, ei << 1 | 1))

        max_flow = 0
        while True:
            bfs = [s]
            depth = [None] * n
            depth[s] = 0
            step = 1
            while bfs:
                nxt = []
                for i in bfs:
                    for j, ei in G[i]:
                        if depth[j] is not None: continue  # visited
                        if flow[ei] == cap[ei]: continue  # 此路徑流量已滿
                        depth[j] = step
                        if j == t: break  # 到終點，bfs 結束
                        nxt.append(j)
                    else: continue  # 未到終點，繼續 bfs 下個節點
                    break  # 到終點，bfs 結束
                else:  # 未到終點，繼續 bfs 下一輪
                    bfs = nxt
                    step += 1
                    continue
                break  # 到終點，bfs 結束
            else: break  # 未到終點，結束 Dinic 演算法

            max_flow += dfs(s, inf)
        return max_flow

    n, m = map(int, e().split())
    es = []
    for _ in range(m):
        a, b, w = map(int, e().split())
        es.append((a - 1, b - 1, w))

    print(dinic(n, es, 0, n-1))
main()