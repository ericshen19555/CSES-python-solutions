def main():
    from sys import stdin
    from operator import mul
    e = stdin.readline
    mod = 10**9 + 7

    def matmul(a, b):
        b = list(zip(*b))
        return [[sum(map(mul, row, col)) % mod for col in b] for row in a]

    n, m, k = map(int, e().split())
    ans = [[1] + [0] * (n - 1)]
    dp = [[0] * n for _ in range(n)]
    for _ in range(m):
        a, b = map(int, e().split())
        a, b = a-1, b-1
        dp[a][b] += 1

    while k:
        if k & 1:
            ans = matmul(ans, dp)
        dp = matmul(dp, dp)
        k >>= 1
    print(ans[0][-1])
main()