def main():
    from sys import stdin
    e = stdin.readline

    n, m = map(int, e().split())
    es, si = [], []
    for i in range(m):
        a, b, w = map(int, e().split())
        es.append((a - 1, b - 1))
        si.append(w << 20 | i)
    si.sort()

    mst = 0
    ans = [0] * m
    dsu = [-1] * n
    siz = [1] * n
    l = [0] * n
    for x in si:
        w, ei = x >> 20, x & 0xfffff
        a, b = es[ei]
        v = 0
        while a != b:
            if siz[a] < siz[b]: a, b = b, a
            if dsu[b] < 0:
                while dsu[a] >= 0: a = dsu[a]
                l[b] = w
                mst += w
                siz[a] += siz[b]
                dsu[b] = a
                break
            v = max(v, l[b])
            b = dsu[b]
        else:
            ans[ei] = w - v
    print(*[mst + v for v in ans], sep="\n")
main()