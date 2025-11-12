def main():
    from sys import stdin
    e = stdin.readline

    n = int(e())
    G = [[] for _ in range(n)]
    for Gi in G:
        for j, v in enumerate(e()):
            if v == "o":
                Gi.append(j)

    def dfs(i):
        for j in G[i]:
            if vis[j]: continue
            vis[j] = True
            if pr[~j] == -1 or dfs(pr[~j]):
                pr[~j] = i
                return True
        return False

    pr = [-1] * (n << 1)
    ans = 0
    for i in range(n):
        vis = [False] * n
        ans += dfs(i)
    print(ans)

    for i in range(n):
        if ~pr[~i]: pr[pr[~i]] = i

    q = []
    vis = [False] * (n << 1)
    for i in range(n):
        if ~pr[i]: continue
        vis[i] = True
        q.append(i)

    for i in q:
        for j in G[i]:
            if pr[i] == j: continue
            if not vis[~j]:
                vis[~j] = True
                if ~pr[~j] and not vis[pr[~j]]:
                    vis[pr[~j]] = True
                    q.append(pr[~j])
    for i in range(n):
        if not vis[i]:
            print(1, i + 1)
    for i in range(n):
        if vis[~i]:
            print(2, i + 1)
main()