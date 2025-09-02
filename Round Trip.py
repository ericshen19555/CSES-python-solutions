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
    for i, it in enumerate(G):
        G[i] = iter(it)

    pa = [-1] * n
    vis = [False] * n
    for i, v in enumerate(vis):
        if v: continue
        vis[i] = True
        stk = [i]
        while stk:
            i = stk.pop()
            p = pa[i]
            for j in G[i]:
                if j == p: continue
                if vis[j]:
                    ans = [j + 1]
                    while i != j:
                        ans.append(i + 1)
                        i = pa[i]
                    ans.append(j + 1)
                    print(len(ans))
                    print(*ans)
                    return
                else:
                    stk.append(i)
                    pa[j] = i
                    stk.append(j)
                    vis[j] = True
                    break
    print("IMPOSSIBLE")
main()