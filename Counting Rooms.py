def main():
    from sys import stdin
    e = stdin.readline

    def find(x):
        if dsu[x] < 0:
            return x
        dsu[x] = find(dsu[x])
        return dsu[x]

    def merge(a, b) -> bool:
        a, b = find(a), find(b)
        if a == b: return False
        if dsu[a] == dsu[b]: dsu[a] -= 1
        elif dsu[a] > dsu[b]: a, b = b, a
        dsu[b] = a
        return True

    m, n = map(int, e().split())
    n += 1
    area = m * n
    dsu = [0] * (area + n)
    ans = 0
    for r in range(0, area, n):
        for i, c in enumerate(e(), r):
            if c != ".": continue
            dsu[i] = -1
            ans += 1
            if dsu[i - 1]: ans -= merge(i, i - 1)
            if dsu[i - n]: ans -= merge(i, i - n)
    print(ans)
main()