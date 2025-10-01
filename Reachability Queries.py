def main():
    from sys import stdin
    from sys import setrecursionlimit
    setrecursionlimit(5 * 10**4 + 10)
    e = stdin.readline

    def tarjan(i):
        nonlocal dfnn
        dfnn += 1
        dfn[i] = low[i] = dfnn
        stk.append(i);
        instk[i] = True
        for j in G[i]:
            if not instk[j] and dfn[j]: continue
            if not dfn[j]: tarjan(j)
            if low[j] < low[i]: low[i] = low[j]
        if low[i] == dfn[i]:
            j = -1
            while j != i:
                p = j
                j = stk.pop();
                instk[j] = False
                nn[j] = p
                scc[j] = i

    n, m, q = map(int, e().split())
    G = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, e().split())
        a, b = a - 1, b - 1
        G[a].append(b)

    dfn = [0] * n
    low = [0] * n
    scc = [0] * n
    nn = [0] * n
    stk = []
    instk = [False] * n
    dfnn = 0

    bits = [1 << i for i in range(n)]
    for i in range(n):
        if not dfn[i]: tarjan(i)

    R = [[] for _ in range(n)]
    indeg = [0] * n
    for r in range(n):
        if scc[r] != r:
            indeg[r] = -1
            continue
        i = r
        while ~i:
            for j in G[i]:
                j = scc[j]
                if j == r: continue
                R[j].append(r)
                indeg[r] += 1
            i = nn[i]

    qu = [i for i in range(n) if indeg[i] == 0]
    for i in qu:
        bi = bits[i]
        for j in R[i]:
            bits[j] |= bi
            indeg[j] -= 1
            if indeg[j] == 0:
                qu.append(j)

    ans = []
    for _ in range(q):
        a, b = map(int, e().split())
        a, b = a - 1, b - 1
        ans.append("YES" if (bits[scc[a]] >> scc[b]) & 1 else "NO")
    print("\n".join(ans))
main()