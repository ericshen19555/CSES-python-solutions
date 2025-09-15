def main():
    from sys import stdin
    from operator import mul
    e = stdin.readline
    mod = 10**9 + 7

    def matmul(a, b):
        return [[sum(map(mul, row, col)) % mod for col in zip(*b)] for row in a]

    n = int(e())
    ans = [[1], [0]]
    dp = [[1, 1], [1, 0]]
    while n:
        if n & 1:
            ans = matmul(dp, ans)
        dp = matmul(dp, dp)
        n >>= 1
    print(ans[1][0])
main()