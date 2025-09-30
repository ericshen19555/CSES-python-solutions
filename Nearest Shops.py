def main():
    from sys import stdin
    e = stdin.readline

    n, m, k = map(int, e().split())
    cur = [(int(v) - 1, ) * 2 for v in e().split()]
    G = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, e().split())
        a, b = a-1, b-1
        G[a].append(b)
        G[b].append(a)

    dis = [[-1, -1] for _ in range(n)]
    p = [[-1, -1] for _ in range(n)]
    step = 1
    while cur:
        nxt = []
        for i, s in cur:
            for j in G[i]:
                a, b = p[j]
                if a == -1:
                    dis[j][0] = step
                    p[j][0] = s
                    nxt.append((j, s))
                elif a != s and b == -1:
                    dis[j][1] = step
                    p[j][1] = s
                    nxt.append((j, s))
        step += 1
        cur = nxt
    print(*[dis[i][p[i][0] == i] for i in range(n)])
main()