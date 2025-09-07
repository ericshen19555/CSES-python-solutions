def main():
    from sys import stdin
    e = stdin.readline

    def pack(a, b):
        return a << 20 | b

    def unpack(x):
        return x >> 20, x & 0xfffff

    n, q = map(int, e().split())
    l = list(map(int, e().split())) + [0x3f3f3f3f]
    sl = [pack(l[i], i) for i in range(n + 1)]
    sl.sort()
    qs = []
    sq = []
    for i in range(q):
        a, b, c, d = map(int, e().split())
        qs.append((a-1, b))
        sq.append(pack(c-1, i << 1 | 1))
        sq.append(pack(d, i << 1))
    sq.sort()

    ans = [0] * q
    bit = [0] * (n + 1)
    qi = 0
    for i in sl:
        v, i = unpack(i)
        v <<= 20
        while qi < q * 2 and sq[qi] < v:
            ai = sq[qi] & 0xfffff
            sign = -1 if ai & 1 else 1
            ai >>= 1
            s, t = qs[ai]
            res = 0
            while t > s:
                res += bit[t]
                t &= t-1
            while s > t:
                res -= bit[s]
                s &= s-1
            ans[ai] += res * sign
            qi += 1
        i += 1
        while i <= n:
            bit[i] += 1
            i += i & -i
    print("\n".join(map(str, ans)))
main()