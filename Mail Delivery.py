def main():
    from sys import stdin
    e = stdin.readline

    n, m = map(int, e().split())
    G = [[] for _ in range(n)]
    es = []
    deg = [0] * n
    for i in range(m):
        a, b = map(int, e().split())
        a, b = a-1, b-1
        deg[a] ^= 1
        deg[b] ^= 1
        es.append(a ^ b)
        G[a].append(i)
        G[b].append(i)

    if any(deg):
        print("IMPOSSIBLE")
        return

    for i, it in enumerate(G):
        G[i] = iter(it)

    ans = []
    stk = [0]
    while stk:
        i = stk[-1]
        for ei in G[i]:
            if es[ei] == 0: continue
            j = es[ei] ^ i
            es[ei] = 0
            stk.append(j)
            break
        else:
            stk.pop()
            ans.append(i + 1)

    if any(es):
        print("IMPOSSIBLE")
        return

    print(*ans)
main()