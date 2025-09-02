def main():
    from sys import stdin
    inf = float("INF")
    e = stdin.readline

    n, m = map(int, e().split())
    G = [[] for _ in range(n)]
    for _ in range(m):
        a, b, w = map(int, e().split())
        a, b = a-1, b-1
        G[a].append((b, w))

    dis = [inf] * n
    cnt = [0] * n
    inq = [False] * n
    pre = [-1] * n
    for i, v in enumerate(dis):
        if v is not inf: continue
        dis[i] = 0
        q = [i]
        inq[i] = True
        for i in q:
            inq[i] = False
            v, nc = dis[i], cnt[i] + 1
            for j, nv in G[i]:
                nv += v
                if nv < dis[j]:
                    pre[j] = i
                    dis[j] = nv
                    cnt[j] = nc
                    if nc >= n:
                        for _ in range(n + 1):
                            j = pre[j]
                        s = j
                        cycle = [s + 1]
                        i = pre[j]
                        while i != s:
                            cycle.append(i + 1)
                            i = pre[i]
                        cycle.append(s + 1)
                        print("YES")
                        print(*reversed(cycle))
                        return
                    if not inq[j]:
                        q.append(j)
                        inq[j] = True
    print("NO")
main()