def main():
    from sys import stdin
    e = stdin.readline

    n, m = map(int, e().split())
    G = [[] for _ in range(n)]
    es = [0] * m
    for i in range(m):
        a, b = map(int, e().split())
        a, b = a-1, b-1
        es[i] = a ^ b
        G[a].append(i)
        G[b].append(i)

    stk = [0]
    ans = [-1] * m
    vis = [False] * n
    it = [0] * n
    while stk:
        i = stk[-1]
        while it[i] < len(G[i]):
            ei = G[i][it[i]]
            it[i] += 1
            if ~ans[ei]: continue
            ans[ei] = i
            j = es[ei] ^ i
            ans.append(f"{i+1} {j+1}")
            stk.append(j)
            break
        else:
            stk.pop()
            vis[i] = True

    if not all(vis):
        return print("IMPOSSIBLE")

    q = [0]
    for i in q:
        for ei in G[i]:
            j = ans[ei]
            if j == i: continue
            if not vis[j]: continue
            vis[j] = False
            q.append(j)
    if any(vis):
        return print("IMPOSSIBLE")

    print("\n".join(f"{ans[ei] + 1} {(es[ei] ^ ans[ei]) + 1}" for ei in range(m)))
main()