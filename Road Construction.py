def main():
    from sys import stdin
    e = stdin.readline

    def find(x):
        if dsu[x] < 0:
            return x
        dsu[x] = find(dsu[x])
        return dsu[x]

    def merge(a, b):
        a, b = find(a), find(b)
        if a == b: return 0
        if dsu[a] > dsu[b]: a, b = b, a
        dsu[a] += dsu[b]
        dsu[b] = a
        return -dsu[a]

    n, m = map(int, e().split())
    dsu = [-1] * n
    cur = 1
    ans = []
    for _ in range(m):
        a, b = map(int, e().split())
        ret = merge(a-1, b-1)
        if ret:
            n -= 1
            cur = max(ret, cur)
        ans.append(f"{n} {cur}")
    print("\n".join(ans))
main()