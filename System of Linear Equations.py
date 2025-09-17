def main():
    from sys import stdin
    e = stdin.readline
    mod = 10**9 + 7

    n, m = map(int, e().split())
    l = [list(map(int, e().split())) for _ in range(n)]
    for i in range(n):
        for j in range(min(i, m)):
            mul = -l[i][j] * pow(l[j][j], -1, mod) % mod
            for k in range(j, m + 1):
                l[i][k] = (l[i][k] + l[j][k] * mul) % mod
    ans = [0] * m
    for i in range(m - 1, n - 1, -1):
        if l[-1][i]:
            ans[i] = l[-1][m] * pow(l[-1][i], -1, mod) % mod
            break
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, m):
            l[i][m] -= l[i][j] * ans[j]
        if l[i][m]:
            if i >= m or not l[i][i]:
                return print(-1)
            ans[i] = l[i][m] * pow(l[i][i], -1, mod) % mod
    print(*ans)
main()