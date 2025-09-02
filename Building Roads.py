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
        if a == b: return False
        if dsu[a] == dsu[b]: dsu[a] -= 1
        elif dsu[a] > dsu[b]: a, b = b, a
        dsu[b] = a
        return True

    n, m = map(int, e().split())
    dsu = [-1] * n
    r = n
    for _ in range(m):
        a, b = map(int, e().split())
        r -= merge(a - 1, b - 1)
    print(r - 1)
    it = (i for i, v in enumerate(dsu, 1) if v < 0)
    x = next(it)
    print("\n".join(f"{x} {i}" for i in it))
main()