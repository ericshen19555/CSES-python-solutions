mod = 10**9 + 7

def main():
    s = input()
    n = len(s)

    lim = n // 2 + 1
    C = [[0] * lim for _ in range(lim)]
    C[0][0] = 1
    for i in range(1, lim):
        C[i][0] = 1
        for j in range(1, i + 1):
            C[i][j] = (C[i - 1][j] + C[i - 1][j - 1]) % mod

    dp = [[0] * i + [1] for i in range(1, n + 1)]
    for r in range(1, n):
        for i in range(n - r):
            j = i + r
            x = 0
            for k in range(i + 1, j + 1):
                if s[i] == s[k]:
                    x += (dp[k-1][i+1] * dp[j][k+1] % mod) * C[j - i + 1 >> 1][k - i + 1 >> 1] % mod
            dp[j][i] = x % mod
    print(dp[-1][0])
main()