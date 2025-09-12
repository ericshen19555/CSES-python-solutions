def main():
    from sys import stdin
    e = stdin.readline

    n, q = map(int, e().split())
    l = list(map(int, e().split()))
    G = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = map(int, e().split())
        a, b = a-1, b-1
        G[a].append(b)
        G[b].append(a)
    for i, it in enumerate(G):
        G[i] = iter(it)

    stk = [0]
    bit = [0] * (n + 1)
    tin = [0] * n
    tout = [0] * n
    pa = [-1] * n
    tin[0] = 0
    bit[1] = l[0]
    t = 1
    while stk:
        i = stk[-1]
        for j in G[i]:
            if j == pa[i]: continue
            tin[j] = t
            t += 1
            bit[t] = l[j]
            pa[j] = i
            stk.append(j)
            break
        else:
            stk.pop()
            tout[i] = t

    for i in range(1, n):
        ii = i + (i & -i)
        if ii <= n:
            bit[ii] += bit[i]

    ans = []
    for _ in range(q):
        o, *oo = map(int, e().split())
        if o == 1:
            i, v = oo
            i -= 1
            d = v - l[i]
            l[i] = v
            i = tin[i] + 1
            while i <= n:
                bit[i] += d
                i += i & -i
        else:
            i = oo[0] - 1
            s, t = tin[i], tout[i]
            res = 0
            while t > s:
                res += bit[t]
                t &= t-1
            while s > t:
                res -= bit[s]
                s &= s-1
            ans.append(res)
    print("\n".join(map(str, ans)))
main()
