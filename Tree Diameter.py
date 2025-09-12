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

    flag[i] = 0
    cur = [i]
    ans = -1
    while cur:
        nxt = []
        for i in cur:
            for j in G[i]:
                if flag[j] == 0: continue
                flag[j] ^= 1
                nxt.append(j)
        cur = nxt
        ans += 1
    print(ans)
main()