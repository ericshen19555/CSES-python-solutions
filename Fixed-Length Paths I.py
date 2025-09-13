def main():
    from sys import stdin
    from sys import setrecursionlimit
    e = stdin.readline

    setrecursionlimit(2 * 10**5 + 10)

    n, k = map(int, e().split())
    G = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = map(int, e().split())
        a, b = a-1, b-1
        G[a].append(b)
        G[b].append(a)

    siz = [0] * n
    done = [False] * n
    dis = [0] * n

    def dfs_siz(i, pa):
        siz[i] = 1
        for j in G[i]:
            if j == pa or done[j]: continue
            dfs_siz(j, i)
            siz[i] += siz[j]

    def find_cen(i, pa, half):
        for j in G[i]:
            if j != pa and not done[j] and siz[i] > half:
                return find_cen(j, i, half)
        return i

    def dfs_add(i, pa, dep, v):
        dis[dep] += v
        for j in G[i]:
            if j == pa or done[j]: continue
            dfs_add(j, i, dep + 1, v)

    def dfs_que(i, pa, dep):
        nonlocal ans
        if k >= dep: ans += dis[k - dep]
        for j in G[i]:
            if j == pa or done[j]: continue
            dfs_que(j, i, dep + 1)

    def cen_decomp(i):
        dfs_siz(i, -1)
        c = find_cen(i, -1, siz[i] >> 1)
        dis[0] = 1
        for j in G[c]:
            if done[j]: continue
            dfs_que(j, c, 1)
            dfs_add(j, c, 1, 1)
        dfs_add(c, -1, 0, -1)
        done[c] = True
        for j in G[c]:
            if done[j]: continue
            cen_decomp(j)

    ans = 0
    cen_decomp(0)

    print(ans)
main()