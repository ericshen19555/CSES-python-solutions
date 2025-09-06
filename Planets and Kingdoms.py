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
            scn += 1
            j = -1
            while j != i:
                j = stk.pop()
                instk[j] = False
                scc[j] = scn

    n, m = map(int, e().split())
    G = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, e().split())
        a, b = a-1, b-1
        G[a].append(b)

    dfn = [0] * n
    low = [0] * n
    scc = [0] * n
    stk = []
    instk = [False] * n
    dfnn = scn = 0
    for i in range(n):
        if not dfn[i]:
            tarjan(i)
    print(scn)
    print(*scc)
main()