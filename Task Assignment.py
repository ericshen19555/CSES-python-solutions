def main():
    from sys import stdin
    e = stdin.readline
    inf = float("INF")

    def KM(g):  # 完全二分圖最小權完美匹配
        n = len(g)

        l = [0] * (n * 2 + 1)
        pr = [n] * (n + 1)
        pre = [0] * n
        for s in range(n):
            p = n
            pr[p] = s
            slack = [inf] * n
            vis = [0] * (n + 1)
            while True:
                vis[p] = True
                i = pr[p]
                delta = inf
                for j in range(n):
                    if vis[j]: continue
                    d = g[i][j] - l[i] - l[~j]
                    if d < slack[j]:
                        slack[j] = d
                        pre[j] = p
                    if slack[j] < delta:
                        delta = slack[j]
                        q = j
                for j in range(n + 1):
                    if vis[j]:
                        l[pr[j]] += delta
                        l[~j] -= delta
                    else:
                        slack[j] -= delta
                p = q
                if pr[p] == n: break
            q = 0
            while q < n:
                q = pre[p]
                pr[p] = pr[q]
                p = q

        return -l[n], pr

    n = int(e())
    l = [list(map(int, e().split())) for _ in range(n)]
    ans, pr = KM(l)
    print(ans)
    print("\n".join(f"{pr[j] + 1} {j + 1}" for j in range(n) if ~pr[j]))
main()
