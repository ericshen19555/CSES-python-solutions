# dominator tree, approximately O(n log n)
# TODO: optimize: https://cses.fi/problemset/hack/1703/entry/11872565/, https://cses.fi/problemset/hack/1703/entry/10015779/

def main():
    from sys import stdin
    e = stdin.readline

    n, m = map(int, e().split())
    G = [[] for _ in range(n)]
    R = [[] for _ in range(n)]
    D = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, e().split())
        a, b = a - 1, b - 1
        G[a].append(b)
        R[b].append(a)

    dfn = [-1] * n
    pa = [-1] * n
    stk = [0]
    it = [0] * n
    path = []
    while stk:
        i = stk[-1]
        if it[i] == 0:
            dfn[i] = len(path)
            path.append(i)
        if it[i] < len(G[i]):
            j = G[i][it[i]]
            it[i] += 1
            if ~pa[j]: continue
            pa[j] = i
            stk.append(j)
        else:
            stk.pop()

    def find(x):
        if top[x] == x: return x
        p = top[x]
        top[x] = find(p)
        if dfn[sdm[best[p]]] < dfn[sdm[best[x]]]:
            best[x] = best[p]
        return top[x]

    idm = [-1] * n
    top = list(range(n))
    sdm = list(range(n))
    best = list(range(n))
    for i in reversed(path):
        if i == 0: continue
        res = n
        for j in R[i]:
            if dfn[j] == -1: continue
            find(j)
            res = min(res, dfn[j if dfn[j] < dfn[i] else sdm[best[j]]])
        sdm[i] = path[res]
        top[i] = pa[i]
        D[sdm[i]].append(i)
        i = pa[i]
        for j in D[i]:
            find(j)
            idm[j] = i if sdm[best[j]] == i else best[j]
        del D[i][:]
    for i in path:
        if i == 0: continue
        if idm[i] != sdm[i]:
            idm[i] = idm[idm[i]]
    key = [False] * n
    i = n - 1
    while ~i:
        key[i] = True
        i = idm[i]
    ans = [i + 1 for i, v in enumerate(key) if v]
    print(len(ans))
    print(*ans)
main()