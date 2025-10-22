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

    def find(x):
        if dsu[x] < 0:
            return x
        dsu[x] = find(dsu[x])
        return dsu[x]

    def merge(a, b):
        a, b = find(a), find(b)
        if a == b: return False
        if dsu[a] == dsu[b]: dsu[a] -= 1
        elif dsu[a] > dsu[b]: a, b = b, a
        dsu[b] = a
        return True

    ans = [""] * m
    dsu = [-1] * n
    pending = []
    pw = 0
    for x in si:
        w, i = x >> 20, x & 0xfffff
        if pw != w:
            for x in pending: merge(*x)
            pending.clear()
            pw = w
        a, b = es[i]
        ans[i] = "YES" if find(a) != find(b) else "NO"
        pending.append((a, b))
    print("\n".join(ans))
main()