def main():
    from sys import stdin
    e = stdin.readline

    n, m = map(int, e().split())
    G = [[] for _ in range(n)]
    deg = [0] * n
    deg[0] -= 1
    deg[-1] += 1
    for _ in range(m):
        a, b = map(int, e().split())
        a, b = a-1, b-1
        G[a].append(b)
        deg[a] += 1
        deg[b] -= 1
    if any(deg):
        print("IMPOSSIBLE")
        return

    for i, it in enumerate(G):
        G[i] = iter(it)

    ans = []
    stk = [0]
    while stk:
        i = stk[-1]
        for j in G[i]:
            stk.append(j)
            break
        else:
            stk.pop()
            ans.append(i + 1)
    if len(ans) <= m:
        print("IMPOSSIBLE")
        return
    print(*reversed(ans))
main()