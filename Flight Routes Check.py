def main():
    from sys import stdin
    e = stdin.readline

    n, m = map(int, e().split())
    G = [[] for _ in range(n)]
    R = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, e().split())
        a, b = a-1, b-1
        G[a].append(b)
        R[b].append(a)

    q = [0]
    vis = [False] * n
    vis[0] = True
    for i in q:
        for j in G[i]:
            if vis[j]: continue
            vis[j] = True
            q.append(j)
    if len(q) < n:
        print("NO")
        print(f"{1} {vis.index(False) + 1}")
        return

    q = [0]
    vis = [False] * n
    vis[0] = True
    for i in q:
        for j in R[i]:
            if vis[j]: continue
            vis[j] = True
            q.append(j)
    if len(q) < n:
        print("NO")
        print(f"{vis.index(False) + 1} {1}")
        return

    print("YES")
main()