"""
先將 k 質因數分解為 Pi p^e
再分別對每個 p 計算 "all(max(a, b) == e for a, b in pairwise(arr))" 的 arr 數量
可以用 DP:
dp[i][0]: 最後一個數字 = [0, e)
dp[i][1]: 最後一個數字 = e
dp[0] = (0, 1)
dp[1] = (e, 1)
dp[2] = (e, e + 1)
...
dp[i] = (dp[i-1][1] * e, sum(dp[i-1]))
"""

def main():
    from sys import stdin
    e = stdin.readline
    mul = lambda a, b: a * b % mod
    mod = 10**9 + 7

    def matmul(a, b):
        b = tuple(zip(*b))
        return [[sum(map(mul, row, col)) for col in b] for row in a]

    lim = int(10 ** 4.5) + 1
    sieve = [True] * lim
    sieve[0] = sieve[1] = False
    ps = []
    for i, v in enumerate(sieve):
        if not v: continue
        ps.append(i)
        for j in range(i * i, lim, i):
            sieve[j] = False

    ans = []
    for _ in range(int(e())):
        n, k = map(int, e().split())
        res = 1
        pi = 0
        while k > 1:
            cnt = 0
            if pi < len(ps):
                p = ps[pi]
                while k % p == 0:
                    k //= p
                    cnt += 1
            else:
                cnt = k = 1
            if cnt:
                dp = [[0, 1]]
                aux = [[0, 1], [cnt, 1]]
                x = n
                while x:
                    if x & 1:
                        dp = matmul(dp, aux)
                    aux = matmul(aux, aux)
                    x >>= 1
                res *= dp[0][0] + dp[0][1]
                res %= mod
            pi += 1
        ans.append(res)
    print(*ans, sep="\n")
main()