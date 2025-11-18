mod = 10 ** 9 + 7

def main():
    from sys import stdin
    e = stdin.readline

    n, lim = map(int, e().split())
    lim += 1
    l = sorted(map(int, e().split()))
    m = n + 1 >> 1

    d = [[0] * lim for _ in range(m + 1)]
    d[0][0] = 1
    pv = 0
    for i, v in enumerate(l):
        p = [[0] * lim for _ in range(m + 1)]
        dv = v - pv
        for j in range(m + 1):
            jd = j * dv
            for k in range(lim):
                x = d[j][k] % mod
                if not x: continue
                nk = k + jd
                if nk >= lim: continue
                p[j][nk] += (j + 1) * x % mod
                if j > 0: p[j - 1][nk] += j * x % mod
                if j < m: p[j + 1][nk] += x
        pv = v
        d = p
    print(sum(d[0]) % mod)
main()
