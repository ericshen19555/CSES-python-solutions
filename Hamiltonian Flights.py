def main():
    from sys import stdin
    mod = 10**9 + 7
    e = stdin.readline

    n, m = map(int, e().split())
    bit = 1 << n

    G = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, e().split())
        a, b = a-1, b-1
        G[a].append(b)

    dp = [[0] * n for _ in range(bit)]
    dp[0b1][0] = 1
    for b in range(1, bit):
        for i in range(n):
            x = dp[b][i] % mod
            if x == 0: continue
            for j in G[i]:
                if (b >> j) & 1: continue
                dp[b | (1 << j)][j] += x
    print(dp[-1][-1] % mod)
main()