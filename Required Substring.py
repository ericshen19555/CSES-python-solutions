def main():
    from sys import stdin
    from string import ascii_uppercase as A
    e = stdin.readline
    mod = 10**9 + 7

    m = int(e())
    s = e().rstrip()
    n = len(s)

    lps = [0] * n
    j = 0
    for i in range(1, n):
        c = s[i]
        while j and s[j] != c:
            j = lps[j - 1]
        j += (s[j] == c)
        lps[i] = j

    step = [[0] * 26 for _ in range(n)]
    for i in range(n):
        for ci, c in enumerate(A):
            if s[i] == c:
                step[i][ci] = i + 1
            else:
                step[i][ci] = step[lps[i - 1]][ci]

    dp = [[0] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = 1
    ans = 0
    for i in range(m):
        for j in range(n):
            x = dp[i][j] % mod
            if not x: continue
            for ci in range(len(A)):
                dp[i + 1][step[j][ci]] += x
        ans += dp[i][n] * pow(len(A), m - i, mod)
    ans += dp[m][n]
    print(ans % mod)
main()