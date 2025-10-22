def main():
    from sys import stdin
    e = stdin.readline

    n, m = map(int, e().split())
    G = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, e().split())
        a, b = a - 1, b - 1
        G[a].append(b)
        G[b].append(a)

    ans = n + 1
    pa = [-1] * n
    for s in range(n):
        q = [s]
        dis = [-1] * n
        dis[s] = 0
        pa[s] = s
        for i in q:
            for j in G[i]:
                if j == pa[i]: continue
                if ~dis[j]:
                    ans = min(ans, dis[i] + dis[j] + 1)
                    if ans == 3:
                        print(ans)
                        return
                else:
                    dis[j] = dis[i] + 1
                    pa[j] = i
                    q.append(j)
    print(ans if ans <= n else -1)
main()