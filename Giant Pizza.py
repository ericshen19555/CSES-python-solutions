def main():
    from sys import stdin
    from sys import setrecursionlimit
    e = stdin.readline

    setrecursionlimit(2 * 10**5 + 10)

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

    m, n = map(int, e().split())
    n <<= 1
    G = [[] for _ in range(n)]
    for _ in range(m):
        sa, a, sb, b = e().split()
        a, b = int(a) - 1, int(b) - 1
        a, b = a << 1 | (sa == "+"), b << 1 | (sb == "+")
        G[a ^ 1].append(b)
        G[b ^ 1].append(a)

    dfn = [0] * n
    low = [0] * n
    scc = [0] * n
    stk = []
    instk = [False] * n
    dfnn = scn = 0
    for i in range(n):
        if not dfn[i]:
            tarjan(i)

    it = iter(scc)
    if any(a == b for a, b in zip(it, it)):
        print("IMPOSSIBLE")
    else:
        it = iter(scc)
        print(" ".join("-+"[a > b] for a, b in zip(it, it)))
main()