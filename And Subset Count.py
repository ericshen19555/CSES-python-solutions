def main():
    from sys import stdin
    e = stdin.readline
    mod = 10**9 + 7

    n = int(e())
    l = list(map(int, e().split()))
    bl = n.bit_length()

    pow2 = [1] * (n + 1)
    for i in range(n):
        pow2[i + 1] = pow2[i] * 2 % mod

    bit = 1 << bl
    dp = [0] * bit
    for v in l:
        dp[v] += 1
    for k in range(bl):
        b = 0
        bb = 1 << k
        while b < bit:
            b |= bb
            dp[b ^ bb] += dp[b]
            b += 1
    for i in range(bit):
        dp[i] = pow2[dp[i]] - 1
    for k in range(bl):
        b = 0
        bb = 1 << k
        while b < bit:
            b |= bb
            dp[b ^ bb] -= dp[b]
            b += 1

    print(*[dp[i] % mod for i in range(n + 1)])
main()