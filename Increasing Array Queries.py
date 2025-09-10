def main():
    from sys import stdin
    from itertools import accumulate
    e = stdin.readline

    def add(i, v):
        i += 1
        vi = v * i
        while i <= n:
            bit0[i] += v
            bit1[i] += vi
            i += i & -i

    def query(i):
        v = vi = 0
        x = i + 1
        while i:
            v += bit0[i]
            vi += bit1[i]
            i &= i-1
        return x * v - vi

    n, q = map(int, e().split())
    l = list(map(int, e().split()))
    p = list(accumulate(l, initial=0))

    qs = [[] for _ in range(n)]
    for i in range(q):
        s, t = map(int, e().split())
        s -= 1
        qs[s].append((t, i))

    ans = [0] * q
    bit0 = [0] * (n + 1)
    bit1 = [0] * (n + 1)
    stk = []
    pi, pv = n, float("INF")
    for i in range(n - 1, -1, -1):
        v = l[i]
        add(i, v)
        add(pi, -v)
        while pv < v:
            d = v - pv
            add(pi, d)
            pi, pv = stk.pop()
            add(pi, -d)
        stk.append((pi, pv))
        pi, pv = i, v
        for t, ai in qs[i]:
            s = i
            ans[ai] = p[i] - p[t] + query(t) - query(s)
    print("\n".join(map(str, ans)))
main()