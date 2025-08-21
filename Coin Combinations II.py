from sys import stdin

mod = 10 ** 9 + 7
e = stdin.readline

n, m = map(int, e().split())
m += 1
dp = [0] * m
dp[0] = 1
for v in map(int, e().split()):
    for i in range(v, m):
        dp[i] += dp[i - v]
        dp[i] %= mod
print(dp[-1])
