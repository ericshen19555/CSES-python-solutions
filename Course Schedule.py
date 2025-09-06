def main():
    from sys import stdin
    e = stdin.readline

    n, m = map(int, e().split())
    indeg = [0] * n
    G = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, e().split())
        a, b = a-1, b-1
        G[a].append(b)
        indeg[b] += 1

    q = [i for i, v in enumerate(indeg) if v == 0]
    for i in q:
        for j in G[i]:
            indeg[j] -= 1
            if indeg[j] == 0:
                q.append(j)
    print(" ".join(str(i + 1) for i in q) if len(q) == n else "IMPOSSIBLE")
main()