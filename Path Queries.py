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

    stk = [0]
    bit = [0] * (n + 1)
    tin = [0] * n
    tout = [0] * n
    pa = [-1] * n
    t = 0
    while stk:
        i = stk.pop()
        if i >= 0:
            p = pa[i]
            tin[i] = t
            t += 1
            bit[t] += l[i]
            stk.append(~i)
            for j in G[i]:
                if j == p: continue
                pa[j] = i
                stk.append(j)
        else:
            i = ~i
            if t < n: bit[t + 1] -= l[i]
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
            x = tin[i] + 1
            while x <= n:
                bit[x] += d
                x += x & -x
            x = tout[i] + 1
            while x <= n:
                bit[x] -= d
                x += x & -x
        else:
            i = oo[0] - 1
            res = 0
            x = tin[i] + 1
            while x:
                res += bit[x]
                x &= x - 1
            ans.append(res)
    print("\n".join(map(str, ans)))
main()