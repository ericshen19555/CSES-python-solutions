# TODO: optimize https://cses.fi/problemset/hack/1701/entry/6358669/

def main():
    from sys import stdin
    from random import getrandbits
    e = stdin.readline
    SALT = getrandbits(32)
    MASK = (1 << 32) - 1

    def xor_shift(x):
        x ^= x << 13
        x ^= x >> 7
        x ^= x << 17
        x ^= x >> 31
        return x + SALT

    def f(both=False):
        def bfs(s):
            q = [s]
            pa = [-1] * n
            for i in q:
                p = pa[i]
                for j in G[i]:
                    if j == p: continue
                    pa[j] = i
                    q.append(j)
            return q, pa

        G = [[] for _ in range(n)]
        for _ in range(n - 1):
            a, b = map(int, e().split())
            a, b = a - 1, b - 1
            G[a].append(b)
            G[b].append(a)
        q, pa = bfs(0)
        siz = [1] * n
        for i in reversed(q):
            if not i: continue
            p = pa[i]
            siz[p] += siz[i]
        c = 0
        while True:
            p = pa[c]
            for j in G[c]:
                if j == p: continue
                if siz[j] > n >> 1:
                    c = j
                    break
            else: break
        q, pa = bfs(c)
        h = [1] * n
        for i in reversed(q):
            if i == c: continue
            p = pa[i]
            h[p] += xor_shift(h[i]) & MASK
        res = h[c] & MASK
        if not both:
            return res
        if n & 1 == 0:
            p = pa[c]
            for j in G[c]:
                if j == p: continue
                if siz[j] == n >> 1:
                    h[c] -= xor_shift(h[j]) & MASK
                    h[j] += xor_shift(h[c]) & MASK
                    return [res, h[j] & MASK]
        return [res]

    ans = []
    for _ in range(int(e())):
        n = int(e())
        ans.append("YES" if f() in f(True) else "NO")
    print("\n".join(ans))
main()