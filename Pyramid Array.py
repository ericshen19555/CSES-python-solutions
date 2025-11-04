def main():
    from sys import stdin
    e = stdin.readline

    n = int(e())
    l = list(map(int, e().split()))
    bit = [0] * (n + 1)
    sl = sorted(range(n), key=l.__getitem__, reverse=True)
    pv = -1
    ans = 0
    pg = s = 0
    for g in range(n):
        v = l[sl[g]]
        if pv != v:
            for x in range(pg, g):
                i = sl[x] + 1
                res = 0
                while i:
                    res += bit[i]
                    i &= i - 1
                ans += min(res, s - res)
            for x in range(pg, g):
                i = sl[x] + 1
                while i <= n:
                    bit[i] += 1
                    i += i & -i
            s += g - pg
            pv = v
            pg = g
    for x in range(pg, n):
        i = sl[x]
        res = 0
        while i:
            res += bit[i]
            i &= i - 1
        ans += min(res, s - res)
    print(ans)
main()