def main():
    from sys import stdin
    e = stdin.readline
    R = 10**6 + 1

    n = int(e())
    ver = []
    hor = []
    for _ in range(n):
        a, b, c, d = map(int, e().split())
        if a == c:
            if b > d: b, d = d, b
            ver.append((b, a, 1))
            ver.append((d + 1, a, -1))
        else:
            if a > c: a, c = c, a
            hor.append((b, a - 1, c))
    ver.sort()
    hor.sort()
    q = len(hor)

    m = R << 1
    bit = [0] * m
    ans = 0
    qi = 0
    for y, x, v in ver:
        while qi < q and hor[qi][0] < y:
            _, s, t = hor[qi]
            qi += 1
            s, t = R + s, R + t
            while t > s:
                ans += bit[t]
                t &= t - 1
            while s > t:
                ans -= bit[s]
                s &= s - 1
        i = R + x
        while i < m:
            bit[i] += v
            i += i & -i
    print(ans)
main()