def main():
    from sys import stdin
    from operator import add
    e = stdin.readline
    inf = float("INF")

    def matmul(a, b):
        b = list(zip(*b))
        return [[min(map(add, row, col)) for col in b] for row in a]

    n, m, k = map(int, e().split())
    ans = [[0] + [inf] * (n - 1)]
    dp = [[inf] * n for _ in range(n)]
    for _ in range(m):
        a, b, w = map(int, e().split())
        a, b = a-1, b-1
        dp[a][b] = min(dp[a][b], w)

    while k:
        if k & 1:
            ans = matmul(ans, dp)
        dp = matmul(dp, dp)
        k >>= 1
    ans = ans[0][-1]
    print(ans if ans < inf else -1)
main()