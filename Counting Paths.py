def main():
    from sys import stdin
    e = stdin.readline

    n, q = map(int, e().split())
    G = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = map(int, e().split())
        a, b = a-1, b-1
        G[a].append(b)
        G[b].append(a)
    for i, it in enumerate(G):
        G[i] = iter(it)

    ans = [0] * n
    qs = [[] for _ in range(n)]
    for qi in range(q):
        a, b = map(int, e().split())
        a, b = a-1, b-1
        if a == b == 0:
            ans[0] += 1
        else:
            ans[a] += 1
            ans[b] += 1
            qs[a].append(b)
            if a != b: qs[b].append(a)

    def find(x):
        if dsu[x] < 0:
            return x
        dsu[x] = find(dsu[x])
        return dsu[x]

    dsu = [-1] * n
    top = [-1] * n
    pa = [-1] * n
    top[0] = 0
    stk = [0]
    while stk:
        i = stk[-1]
        for j in G[i]:
            if j == pa[i]: continue
            pa[j] = i
            top[j] = j
            for jj in qs[j]:
                if top[jj] == -1: continue
                a = top[find(jj)]
                ans[a] -= 1
                if a: ans[pa[a]] -= 1
            stk.append(j)
            break
        else:
            stk.pop()
            if not i: continue
            p = pa[i]
            ans[p] += ans[i]
            ri, rp = find(i), find(p)
            top[ri] = top[rp]
            if dsu[rp] == dsu[ri]: dsu[rp] -= 1
            elif dsu[rp] > dsu[ri]: rp, ri = ri, rp
            dsu[ri] = rp
    print(" ".join(map(str, ans)))
main()