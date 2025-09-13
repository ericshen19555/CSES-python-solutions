def main():
    from sys import stdin
    e = stdin.readline

    n, k = map(int, e().split())
    pa = [0] * n
    deg = [0] * n
    deg[0] = 2
    for _ in range(n - 1):
        a, b = map(int, e().split())
        a, b = a-1, b-1
        deg[a] += 1
        deg[b] += 1
        pa[a] ^= b
        pa[b] ^= a

    l = [[1] for _ in range(n)]

    ans = 0
    for i in range(n):
        while deg[i] == 1:
            deg[i] = 0
            y = l[i]
            y.append(0)
            p = pa[i]
            x = l[p]
            # merge x y -> x
            if len(x) < len(y): x, y = y, x
            xs, ys = len(x), len(y)
            for idx in range(ys):
                if 0 <= k - idx < xs:
                    ans += x[~(k - idx)] * y[~idx]
            for idx in range(ys):
                x[~idx] += y[~idx]
            l[p] = x
            pa[p] ^= i
            deg[p] -= 1
            i = p
    print(ans)
main()