def main():
    from sys import stdin
    inf = float("INF")
    e = stdin.readline

    n, m, q = map(int, e().split())
    dis = [[inf] * n for _ in range(n)]
    for i, row in enumerate(dis):
        row[i] = 0

    for _ in range(m):
        a, b, w = map(int, e().split())
        a, b = a-1, b-1
        dis[a][b] = dis[b][a] = min(dis[b][a], w)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])

    ans = []
    for _ in range(q):
        a, b = map(int, e().split())
        a, b = a-1, b-1
        ans.append(-1 if dis[a][b] is inf else dis[a][b])
    print("\n".join(map(str, ans)))
main()