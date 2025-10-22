def main():
    from sys import stdin
    from collections import deque
    e = stdin.readline
    inf = float("INF")

    n, m, q = map(int, e().split())
    G = [[] for _ in range(n)]
    qs = [[] for _ in range(q)]
    for _ in range(m):
        a, b = map(int, e().split())
        a, b = a - 1, b - 1
        G[a].append(b)
        G[b].append(a)
    ans = [0] * q
    for i in range(q):
        a, b, x = map(int, e().split())
        a, b = a - 1, b - 1
        qs[a].append(i)
        ans[i] = (b, x)

    m = n << 1
    for s in range(n):
        dis = [inf] * m
        dis[s << 1] = 0
        qu = deque([s << 1])
        while qu:
            i = qu.popleft()
            odd = (i & 1) ^ 1
            for j in G[i >> 1]:
                j = j << 1 | odd
                if dis[j] != inf: continue
                dis[j] = dis[i] + 1
                qu.append(j)
        for i in qs[s]:
            b, x = ans[i]
            ans[i] = "YES" if dis[b << 1 | (x & 1)] <= x else "NO"
    print("\n".join(ans))
main()