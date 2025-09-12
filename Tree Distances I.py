def main():
    from sys import stdin
    e = stdin.readline

    n = int(e())
    G = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = map(int, e().split())
        a, b = a-1, b-1
        G[a].append(b)
        G[b].append(a)

    flag = [0] * n
    flag[0] = 1
    cur = [0]
    while cur:
        nxt = []
        for i in cur:
            for j in G[i]:
                if flag[j] == 1: continue
                flag[j] ^= 1
                nxt.append(j)
        cur = nxt

    dis = [0] * n

    flag[i] = 0
    cur = [i]
    step = 0
    while cur:
        nxt = []
        for i in cur:
            dis[i] = step
            for j in G[i]:
                if flag[j] == 0: continue
                flag[j] ^= 1
                nxt.append(j)
        cur = nxt
        step += 1

    flag[i] = 1
    cur = [i]
    step = 0
    while cur:
        nxt = []
        for i in cur:
            dis[i] = max(dis[i], step)
            for j in G[i]:
                if flag[j] == 1: continue
                flag[j] ^= 1
                nxt.append(j)
        cur = nxt
        step += 1
    print(*dis)
main()