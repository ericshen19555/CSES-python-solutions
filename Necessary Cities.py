def main():
    from sys import stdin
    from sys import setrecursionlimit
    e = stdin.readline
    setrecursionlimit(10**5 + 10)

    def tarjan(i, pa):
        nonlocal dfnn
        dfnn += 1
        dfn[i] = low[i] = dfnn
        ch = 0
        for j in G[i]:
            if not dfn[j]:
                ch += 1
                tarjan(j, i)
                if low[j] < low[i]: low[i] = low[j]
                if i != pa and low[j] >= dfn[i]: ans[i] = True
            elif dfn[j] < low[i]:
                low[i] = dfn[j]
        if i == pa and ch >= 2:
            ans[i] = True

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
    ans = [False] * n
    for i in range(n):
        if not dfn[i]:
            tarjan(i, i)
    print(sum(ans))
    print(" ".join(f"{i + 1}" for i in range(n) if ans[i]))
main()