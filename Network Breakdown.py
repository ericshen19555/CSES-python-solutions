def main():
    from sys import stdin
    e = stdin.readline

    n, m, q = map(int, e().split())
    es = []
    for _ in range(m):
        a, b = map(int, e().split())
        a, b = a - 1, b - 1
        if a > b: a, b = b, a
        es.append((a, b))
    qs = []
    for _ in range(q):
        a, b = map(int, e().split())
        a, b = a - 1, b - 1
        if a > b: a, b = b, a
        qs.append((a, b))
    u = set(qs)

    def find(x):
        if dsu[x] < 0: return x
        dsu[x] = find(dsu[x])
        return dsu[x]

    def merge(a, b):
        a, b = find(a), find(b)
        if a == b: return False
        if dsu[a] > dsu[b]: a, b = b, a
        dsu[a] += dsu[b]
        dsu[b] = a
        return True

    r = n
    dsu = [-1] * n
    for a, b in es:
        if (a, b) in u: continue
        r -= merge(a, b)
    ans = []
    for a, b in reversed(qs):
        ans.append(r)
        r -= merge(a, b)
    print(*ans[::-1])
main()