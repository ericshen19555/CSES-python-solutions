def main():
    from sys import stdin
    e = stdin.readline

    n, q = map(int, e().split())
    l = [[0]] + [[0] + [1 if v == "*" else 0 for v in e().rstrip()] for _ in range(n)]
    bit = [row.copy() for row in l]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            jj = j + (j & -j)
            if jj <= n:
                bit[i][jj] += bit[i][j]
    for i in range(1, n + 1):
        ii = i + (i & -i)
        if ii <= n:
            for j in range(1, n + 1):
                bit[ii][j] += bit[i][j]
    ans = []
    for _ in range(q):
        o, *oo = map(int, e().split())
        if o == 1:
            i, j = oo
            v = -1 if l[i][j] else 1
            l[i][j] += v
            while i <= n:
                jj = j
                while jj <= n:
                    bit[i][jj] += v
                    jj += jj & -jj
                i += i & -i
        else:
            a, b, c, d = oo
            a, b = a-1, b-1
            res = 0
            while c > a:
                s, t = b, d
                while t > s:
                    res += bit[c][t]
                    t &= t-1
                while s > t:
                    res -= bit[c][s]
                    s &= s-1
                c &= c-1
            while a > c:
                s, t = b, d
                while t > s:
                    res -= bit[a][t]
                    t &= t-1
                while s > t:
                    res += bit[a][s]
                    s &= s-1
                a &= a-1
            ans.append(res)
    print("\n".join(map(str, ans)))
main()