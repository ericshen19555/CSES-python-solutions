def main():
    from sys import stdin
    e = stdin.readline

    n, m = map(int, e().split())
    G = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, e().split())
        a, b = a-1, b-1
        G[a].append(b)
    for i, it in enumerate(G):
        G[i] = iter(it)

    vis = [False] * n
    instk = [False] * n
    for i, v in enumerate(vis):
        if v: continue
        vis[i] = True
        instk[i] = True
        stk = [i]
        while stk:
            i = stk[-1]
            for j in G[i]:
                if not instk[i] and vis[j]: continue
                if instk[j]:
                    cycle = stk[stk.index(j):] + [j]
                    print(len(cycle))
                    print(" ".join(str(i + 1) for i in cycle))
                    return
                vis[j] = True
                instk[j] = True
                stk.append(j)
                break
            else:
                stk.pop()
                instk[i] = False
    print("IMPOSSIBLE")
main()