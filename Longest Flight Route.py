def main():
    from sys import stdin
    inf = float("INF")
    e = stdin.readline

    n, m = map(int, e().split())
    G = [[] for _ in range(n)]
    indeg = [0] * n
    for _ in range(m):
        a, b = map(int, e().split())
        a, b = a-1, b-1
        G[b].append(a)
        indeg[a] += 1

    nxt = [(-inf, -1)] * n
    q = [i for i, v in enumerate(indeg) if v == 0]
    nxt[-1] = (0, -1)
    for i in q:
        x = (nxt[i][0] + 1, i)
        for j in G[i]:
            nxt[j] = max(nxt[j], x)
            indeg[j] -= 1
            if indeg[j] == 0:
                q.append(j)

    if nxt[0][0] == -inf:
        print("IMPOSSIBLE")
        return

    ans = []
    i = 0
    while i != -1:
        ans.append(i)
        i = nxt[i][1]
    print(len(ans))
    print(" ".join(str(i + 1) for i in ans))
main()