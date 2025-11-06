def main():
    from sys import stdin
    e = stdin.readline

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

    n, m = map(int, e().split())
    dsu = [-1] * n
    for _ in range(m):
        a, b = map(int, e().split())
        merge(a - 1, b - 1)

    ans = 1
    for v in dsu:
        if v >= 0: continue
        ans |= ans << -v
    print(f"{ans >> 1:b}"[::-1])
main()