def main():
    from sys import stdin
    e = stdin.readline
    mod = 10**9 + 7
    mul = lambda a, b: a * b % mod

    def matmul(a, b):
        return [[sum(map(mul, row, col)) % mod for col in zip(*b)] for row in a]

    ans = []
    t = int(e())
    for _ in range(t):
        n = int(e())
        dp = [[2], [0]]
        trans = [[4, 1], [1, 2]]
        n -= 1
        while n:
            if n & 1:
                dp = matmul(dp, trans)
            trans = matmul(trans, trans)
            n >>= 1
        ans.append(dp[0][0])
    print("\n".join(map(str, ans)))
main()
