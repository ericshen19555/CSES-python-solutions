def main():
    from sys import stdin
    from itertools import accumulate, repeat
    e = stdin.readline

    b = 31
    mod = 10**9 + 7
    mul = lambda x, y: x * y % mod

    n, q = map(int, e().split())
    b_exp = list(accumulate(repeat(b, n), func=mul, initial=1))

    l = [ord(c) - 97 for c in e().rstrip()]
    pre = [0] + list(map(mul, l, b_exp))
    suf = [0] + list(map(mul, l, reversed(b_exp)))
    for i in range(1, n):
        ii = i + (i & -i)
        if ii <= n:
            pre[ii] = (pre[ii] + pre[i]) % mod
            suf[ii] = (suf[ii] + suf[i]) % mod

    ans = []
    for _ in range(q):
        o, s, t = e().split()
        if o == "1":
            i, c = int(s) - 1, ord(t) - 97
            d = c - l[i]
            l[i] = c
            d1 = d * b_exp[i] % mod
            d2 = d * b_exp[~i] % mod
            i += 1
            while i <= n:
                pre[i] = (pre[i] + d1) % mod
                suf[i] = (suf[i] + d2) % mod
                i += i & -i
        else:
            s, t = int(s) - 1, int(t)
            b1, b2 = b_exp[n - t + 1], b_exp[s]
            v1 = v2 = 0
            while t > s:
                v1 += pre[t]
                v2 += suf[t]
                t &= t - 1
            while s > t:
                v1 -= pre[s]
                v2 -= suf[s]
                s &= s - 1
            v1 = (v1 * b1) % mod
            v2 = (v2 * b2) % mod
            ans.append("YES" if v1 == v2 else "NO")
    print("\n".join(ans))
main()