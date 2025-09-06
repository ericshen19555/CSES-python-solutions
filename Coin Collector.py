def main():
    from sys import stdin
    from sys import setrecursionlimit
    e = stdin.readline

    setrecursionlimit(10**5 + 10)

    def tarjan(i):
        nonlocal dfnn, scn
        dfnn += 1
        dfn[i] = low[i] = dfnn
        stk.append(i)
        instk[i] = True
        for j in G[i]:
            if not instk[j] and dfn[j]: continue
            if not dfn[j]: tarjan(j)
            if low[j] < low[i]: low[i] = low[j]
        if low[i] == dfn[i]:
            j = -1
            group = []
            sm = 0
            while j != i:
                j = stk.pop()
                instk[j] = False
                sm += l[j]
                scc[j] = scn
                group.append(j)
            l[i] = sm
            groups.append(group)
            scn += 1

    n, m = map(int, e().split())
    l = list(map(int, e().split()))
    G = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, e().split())
        a, b = a-1, b-1
        G[a].append(b)

    dfn = [0] * n
    low = [0] * n
    scc = [0] * n
    scn = 0
    stk = []
    instk = [False] * n
    groups = []
    dfnn = 0
    for i in range(n):
        if not dfn[i]:
            tarjan(i)

    indeg = [0] * scn
    for group in groups:
        for i in group:
            for j in G[i]:
                if scc[i] == scc[j]: continue
                indeg[scc[j]] += 1

    ans = 0
    dp = [0] * n
    q = [groups[g] for g in range(scn) if indeg[g] == 0]
    for group in q:
        r = group[-1]
        x = l[r] + dp[r]
        ans = max(ans, x)
        for i in group:
            for j in G[i]:
                if scc[i] == scc[j]: continue
                g = scc[j]
                j = groups[g][-1]
                dp[j] = max(dp[j], x)
                indeg[g] -= 1
                if indeg[g] == 0:
                    q.append(groups[g])
    print(ans)
main()