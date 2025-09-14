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

    qs = [[] for _ in range(n)]
    ans = [0] * q
    for qi in range(q):
        a, b = map(int, e().split())
        a, b = a-1, b-1
        if a == b:
            ans[qi] = 0
        else:
            ans[qi] = a ^ b
            qs[a].append(qi)
            qs[b].append(qi)

    def find(x):
        if dsu[x] < 0:
            return x
        dsu[x] = find(dsu[x])
        return dsu[x]

    dsu = [-1] * n
    top = [-1] * n
    dep = [0] * n
    pa = [-1] * n
    stk = [0]
    while stk:
        i = stk.pop()
        if i >= 0:
            top[i] = i
            p, nd = pa[i], dep[i] + 1
            for ai in qs[i]:
                j = ans[ai] ^ i
                if top[j] == -1: continue
                ans[ai] = dep[i] + dep[j] - dep[top[find(j)]] * 2
            stk.append(~i)
            for j in G[i]:
                if j == p: continue
                pa[j] = i
                dep[j] = nd
                stk.append(j)
        else:
            i = ~i
            if not i: continue
            ri, rp = find(i), find(pa[i])
            top[ri] = top[rp]
            if dsu[rp] == dsu[ri]: dsu[rp] -= 1
            elif dsu[rp] > dsu[ri]: rp, ri = ri, rp
            dsu[ri] = rp
    print("\n".join(map(str, ans)))
main()