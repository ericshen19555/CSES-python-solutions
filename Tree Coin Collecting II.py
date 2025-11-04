import sys
from io import StringIO

testcase = """\
4 1
0 0 1 1
1 2
2 3
1 4
3 4
"""

sys.stdin = StringIO(testcase)

def main():
    from sys import stdin
    e = stdin.readline

    n, q = map(int, e().split())
    l = list(map(int, e().split()))
    G = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = map(int, e().split())
        a, b = a - 1, b - 1
        G[a].append(b)
        G[b].append(a)

    # v = l[i]: v & 1 表示自己是否為重要點, v >> 1 表示 i 在無根樹上有多少子樹有 coin
    qu = [0]  # 第一輪 dfs 序，用來建 top
    stk = [0]
    idx = [0] * n  # 遍歷 G[i]
    pa = [-1] * n
    ch = [-1] * n
    siz = [1] * n
    dep = [0] * n
    while stk:
        i = stk[-1]
        p = pa[i]
        it, x = G[i], idx[i]
        if x < len(it):
            j = it[x]
            idx[i] += 1
            if j == p: continue
            qu.append(j)
            pa[j] = i
            dep[j] = dep[i] + 1
            if l[i]: l[j] |= 0b10  # 如果 i 或 i 的祖先有 coin，則更新給 j
            stk.append(j)
        else:
            if l[i] >> 2: l[i] = 1  # 如果無根樹上 >= 2 個子樹有 coin，自己也是重要點
            if ~p:
                l[p] += (l[i] & 1) << 1  # 如果 i 是重要點，則更新給 p
                siz[p] += siz[i]
                if ch[p] == -1 or siz[i] > siz[ch[p]]:
                    ch[p] = i
            stk.pop()
    # l[i]: i 離重要點的最近距離
    l = [0 if v & 1 else n for v in l]
    bfs = [i for i, v in enumerate(l) if v == 0]
    base = len(bfs) - 1 << 1  # 遍歷所有重要點並回到原位的距離
    for i in bfs:
        nv = l[i] + 1
        for j in G[i]:
            if nv < l[j]:
                l[j] = nv
                bfs.append(j)

    dfc = 0
    dfn = [0] * n
    mn = [0] * n  # mn[i]: i 所在重鏈上，l 的前綴 min
    zkw = [0] * (n << 1)  # zkw[dfn[i]]: l 的區間 min
    top = [-1] * n
    for t in qu:
        if ~top[t]: continue
        i = t
        x = n
        while ~i:
            top[i] = t
            dfn[i] = dfc
            mn[i] = x = min(x, l[i])
            zkw[dfc + n] = l[i]
            dfc += 1
            i = ch[i]
    for i in range(n - 1, 0, -1): zkw[i] = min(zkw[i << 1], zkw[i << 1 | 1])

    def lca(a, b):
        res = n
        while top[a] != top[b]:
            if dep[top[a]] < dep[top[b]]: a, b = b, a
            res = min(res, mn[a])
            a = pa[top[a]]
        if dep[a] < dep[b]: a, b = b, a
        s, t = n + dfn[b], n + dfn[a] + 1
        while s < t:
            if s & 1:
                res = min(res, zkw[s])
                s += 1
            if t & 1:
                t -= 1
                res = min(res, zkw[t])
            s >>= 1
            t >>= 1
        return dep[b] - res

    ans = []
    q = 1
    for _ in range(q):
        a, b = map(int, e().split())
        a, b = a - 1, b - 1
        # 2*key + 2*dis_to_key[a] + 2*dis_to_key[b] - dis[a][b] - 2*min(dis_to_key[a...b])
        ans.append(base + (l[a] + l[b] + lca(a, b)) * 2 - dep[a] - dep[b])
    print("\n".join(map(str, ans)))
main()