def main():
    from sys import stdin
    e = stdin.readline

    n, q = map(int, e().split())
    G = [[] for _ in range(n)]
    for i, p in enumerate(map(int, e().split()), 1):
        p -= 1
        G[p].append(i)

    qs = [[] for _ in range(n)]
    ans = [0] * q
    for qi in range(q):
        a, b = map(int, e().split())
        a, b = a-1, b-1
        if a == b:
            ans[qi] = a + 1
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
    pa = [-1] * n
    top = [-1] * n
    stk = [0]
    while stk:
        i = stk.pop()
        if i >= 0:
            top[i] = i
            for ai in qs[i]:
                j = ans[ai] ^ i
                if top[j] == -1: continue
                ans[ai] = top[find(j)] + 1
            stk.append(~i)
            for j in G[i]:
                pa[j] = i
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