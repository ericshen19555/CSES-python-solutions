def main():
    from sys import stdin
    e = stdin.readline

    def tuple(it):
        a, b, w = it
        return w << 40 | (a - 1) << 20 | (b - 1)

    def unpack(x):
        return (x >> 20) & 0xfffff, x & 0xfffff, x >> 40

    n = int(e())
    es = [tuple(map(int, e().split())) for _ in range(n - 1)]
    es.sort(reverse=True)

    def find(x):
        if dsu[x] < 0:
            return x
        dsu[x] = find(dsu[x])
        return dsu[x]

    def merge(a, b):
        if dsu[a] > dsu[b]: a, b = b, a
        dsu[a] += dsu[b]
        dsu[b] = a

    ans = 0
    dsu = [-1] * n
    for a, b, w in map(unpack, es):
        a, b = find(a), find(b)
        ans += w * dsu[a] * dsu[b]
        merge(a, b)
    print(ans)
main()