def main():
    from sys import stdin
    e = stdin.readline

    n, m = map(int, e().split())
    G = [[] for _ in range(n)]
    for _ in range(m):
        a, b, w = map(int, e().split())
        a, b = a-1, b-1
        G[a].append((b, w))

    ans = [float("-INF")] * n
    cnt = [0] * n
    inq = [False] * n
    inf_dis = [False] * n
    ans[0] = 0
    q = [0]
    inq[0] = True
    for i in q:
        if inf_dis[i]: continue
        inq[i] = False
        v = ans[i]
        for j, nv in G[i]:
            nv += v
            if nv > ans[j]:
                ans[j] = nv
                cnt[j] = cnt[i] + 1
                if cnt[j] >= n:
                    inf_dis[j] = True
                    inq[j] = True
                if not inq[j]:
                    q.append(j)
                    inq[j] = True
    q = [i for i, v in enumerate(inf_dis) if v]
    for i in q:
        for j, _ in G[i]:
            if inf_dis[j]: continue
            inf_dis[j] = True
            q.append(j)
    print(-1 if inf_dis[-1] else ans[-1])
main()