def main():
    from sys import stdin
    e = stdin.readline

    n, m = map(int, e().split())
    G = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, e().split())
        a, b = a-1, b-1
        G[a].append(b)
        G[b].append(a)

    color = [0] * n
    for i, v in enumerate(color):
        if v: continue
        v = 1
        cur = [i]
        color[i] = v
        while cur:
            v ^= 3
            nxt = []
            for i in cur:
                for j in G[i]:
                    if color[j]:
                        if color[j] != v:
                            return print("IMPOSSIBLE")
                        continue
                    color[j] = v
                    nxt.append(j)
            cur = nxt
    print(*color)
main()