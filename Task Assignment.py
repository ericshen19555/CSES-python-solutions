def main():
    from sys import stdin
    e = stdin.readline
    inf = float("INF")
    M = 1000

    def KM(l):
        n = len(l)

        def dfs(i: int, aug: bool) -> bool:
            if vis[i]: return False
            vis[i] = True
            for j in range(n):
                if vis[~j]: continue
                d = lx[i] + ly[j] - l[i][j]
                if d == 0:
                    vis[~j] = True
                    if pr[j] == -1 or dfs(pr[j], aug):
                        if aug: pr[j] = i
                        return True
                else:
                    slack[j] = min(slack[j], d)
            return False

        def augment():
            for j in range(n):
                if vis[~j] or slack[j]: continue
                vis[~j] = True
                if pr[j] == -1 or dfs(pr[j], False):
                    return True
            return False

        def relabel():
            d = min((slack[j] for j in range(n) if not vis[~j]), default=inf)
            for i in range(n):
                if vis[i]:
                    lx[i] -= d
            for j in range(n):
                if vis[~j]:
                    ly[j] += d
                else:
                    slack[j] -= d

        lx = list(map(max, l))
        ly = [0] * n
        pr = [-1] * n
        for i in range(n):
            slack = [inf] * n
            vis = [False] * (n << 1)
            if dfs(i, True): continue
            while not augment(): relabel()
            vis = [False] * (n << 1)
            dfs(i, True)

        return pr

    n = int(e())
    l = [[M - int(v) for v in e().split()] for _ in range(n)]
    pr = KM(l)
    print(sum(M - l[pr[j]][j] for j in range(n) if ~pr[j]))
    print("\n".join(f"{pr[j] + 1} {j + 1}" for j in range(n) if ~pr[j]))
main()
