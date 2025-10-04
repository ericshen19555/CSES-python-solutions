def main():
    from sys import stdin
    e = stdin.readline
    lim = 10**7 + 9

    def unpack(x):
        return x >> 12, x & 0xfff

    sqr2 = [-1] * lim
    for a in range(lim):
        if a * a >= lim: break
        aa = a*a
        a_mask = a << 12
        for b in range(a + 1):
            s = aa + b*b
            if s >= lim: break
            sqr2[s] = a_mask | b

    def solve(n):
        for x in range(n + 1):
            if ~sqr2[x] and ~sqr2[n - x]:
                return *unpack(sqr2[x]), *unpack(sqr2[n - x])

    ans = []
    for _ in range(int(e())):
        n = int(e())
        a, b, c, d = solve(n)
        assert a*a + b*b + c*c + d*d == n
        ans.append(f"{a} {b} {c} {d}")
    print("\n".join(ans))
main()