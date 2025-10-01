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
        a, b = a-1, b-1
        r -= merge(a, b)
    print(pow(2, m - n + r, 10**9 + 7))
main()