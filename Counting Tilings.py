def main():
    from sys import stdin
    mod = 10**9 + 7
    e = stdin.readline

    n, m = map(int, e().split())
    k = n + 1
    bit = 1 << k
    d = [0] * bit
    d[0] = 1
    for r in range(m):
        if r:
            p = [0] * bit
            for b in range(bit >> 1):
                p[b << 1] = d[b]
            d = p
        for i in range(n):
            p = [0] * bit
            for b in range(bit):
                # 00     -> 10 01
                # 01, 10 -> 00
                # 11     -> X
                sb = (b >> i) & 3
                if sb == 3: continue
                v = d[b] % mod
                if sb == 0:
                    p[b ^ (1 << i)] += v
                    p[b ^ (1 << i + 1)] += v
                else:  # 1 2
                    p[b ^ (sb << i)] += v
            d = p
    print(d[0] % mod)
main()