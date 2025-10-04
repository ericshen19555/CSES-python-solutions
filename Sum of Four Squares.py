def main():
    from sys import stdin
    e = stdin.readline

    def solve(n):
        if n & 3 == 0:
            if n == 0:
                return (0, 0, 0, 0)
            return tuple(map(lambda x: x << 1, solve(n >> 2)))
        s = int(n ** 0.5)
        if n & 7 in (1, 5):
            a = s - 1 if s & 1 else s
        else:
            a = s if s & 1 else s - 1
        aa = a * a
        bn = n - aa
        for b in range(a + 1):
            bb = b * b
            if bb > bn: break
            cn = bn - bb
            for c in range(b + 1):
                cc = c * c
                if cc > cn: break
                d = int((cn - cc) ** 0.5)
                if cc + d*d == cn:
                    return a, b, c, d

    ans = []
    for _ in range(int(e())):
        n = int(e())
        a, b, c, d = solve(n)
        assert a*a + b*b + c*c + d*d == n
        ans.append(f"{a} {b} {c} {d}")
    print("\n".join(ans))
main()