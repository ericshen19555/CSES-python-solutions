def main():
    from sys import stdin
    from operator import itemgetter
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
    es = [tuple(map(int, e().split())) for _ in range(m)]
    es.sort(key=itemgetter(2))

    ans = 0
    dsu = [-1] * n
    r = n
    for a, b, w in es:
        a, b = a-1, b-1
        if merge(a, b):
            r -= 1
            ans += w
    print(ans if r == 1 else "IMPOSSIBLE")
main()