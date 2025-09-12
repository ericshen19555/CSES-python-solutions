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
    top[0] = 0
    stk = [0]
    while stk:
        i = stk[-1]
        for j in G[i]:
            if j == pa[i]: continue
            pa[j] = i
            dep[j] = dep[i] + 1
            top[j] = j
            for ai in qs[j]:
                jj = ans[ai] ^ j
                if top[jj] == -1: continue
                ans[ai] = dep[j] + dep[jj] - dep[top[find(jj)]] * 2
            stk.append(j)
            break
        else:
            stk.pop()
            if not i: continue
            ri, rp = find(i), find(stk[-1])
            top[ri] = top[rp]
            if dsu[rp] == dsu[ri]: dsu[rp] -= 1
            elif dsu[rp] > dsu[ri]: rp, ri = ri, rp
            dsu[ri] = rp
    print("\n".join(map(str, ans)))
main()