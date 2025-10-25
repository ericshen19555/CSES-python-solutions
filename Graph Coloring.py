def main():
    from sys import stdin
    e = stdin.readline

    n, m = map(int, e().split())
    G = [0] * n
    for _ in range(m):
        a, b = map(int, e().split())
        a, b = a - 1, b - 1
        G[a] |= 1 << b
        G[b] |= 1 << a
    bit = 1 << n
    mask = bit - 1
    dp = [n + 1] * bit
    dp[0] = 0
    best = [-1] * bit
    for b in range(bit):
        if dp[b] > n: continue
        bb = mask ^ b
        while bb:
            lb = bb & -bb
            i = lb.bit_length() - 1
            if G[i] & b == 0:
                nb = b | lb
                dp[nb] = 1
                best[nb] = lb
            bb &= bb - 1
    for b in range(bit):
        x = dp[b]
        if x == 1: continue
        sub = b
        s = best[b]
        while sub:
            nx = dp[sub] + dp[b ^ sub]
            if nx < x:
                x, s = nx, sub
            sub = (sub - 1) & b
        dp[b] = x
        best[b] = s
    print(dp[-1])
    ans = [0] * n
    stk = [(mask, 1)]
    while stk:
        b, c = stk.pop()
        if dp[b] == 1:
            while b:
                i = (b & -b).bit_length() - 1
                ans[i] = c
                b &= b - 1
        elif b:
            s = best[b]
            stk.append((s, c))
            stk.append((b ^ s, c + dp[s]))
    print(*ans)
main()