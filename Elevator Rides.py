def main():
    from sys import stdin
    e = stdin.readline
    ctz = lambda x: (x & -x).bit_length() - 1

    n, k = map(int, e().split())
    l = list(map(int, e().split()))
    bit = 1 << n
    dp = [0] * bit
    rk = [0] * bit
    for b in range(1, bit):
        bb = b
        x, kk = n, 0
        while bb:
            i = ctz(bb)
            v = l[i]
            pb = b ^ (bb & -bb)
            if rk[pb] >= v:
                nx = dp[pb]
                nk = rk[pb] - v
            else:
                nx = dp[pb] + 1
                nk = k - v
            if nx < x or nx == x and nk > kk:
                x = nx
                kk = nk
            bb &= bb - 1
        dp[b], rk[b] = x, kk
    print(dp[-1])
main()