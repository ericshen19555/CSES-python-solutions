def main():
    from sys import stdin
    from sys import setrecursionlimit
    e = stdin.readline
    setrecursionlimit(10**5 + 10)

    def tarjan(i, pa):
        nonlocal dfnn
        dfnn += 1
        dfn[i] = low[i] = dfnn
        for j in G[i]:
            if not dfn[j]:
                tarjan(j, i)
                if low[j] < low[i]: low[i] = low[j]
                if low[j] > dfn[i]: ans.append(f"{i + 1} {j + 1}")
            elif j != pa and dfn[j] < low[i]:
                low[i] = dfn[j]

    n, m = map(int, e().split())
    G = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, e().split())
        a, b = a-1, b-1
        G[a].append(b)
        G[b].append(a)

    dfn = [0] * n
    low = [0] * n
    dfnn = 0
    ans = []
    for i in range(n):
        if not dfn[i]:
            tarjan(i, -1)
    print(len(ans))
    print("\n".join(ans))
main()