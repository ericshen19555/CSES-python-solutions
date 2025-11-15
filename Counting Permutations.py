# OEIS A002464

mod = 10 ** 9 + 7

def main():
    n = int(input())
    if n <= 3:
        print(1 if n == 1 else 0)
        return
    pppp, ppp, pp, p = 1, 1, 0, 0
    for i in range(4, n + 1):
        pppp, ppp, pp, p = ppp, pp, p, ((i + 1) * p - (i - 2) * pp - (i - 5) * ppp + (i - 3) * pppp) % mod
    print(p)
main()

# dp[n][g][i] = num ways to place 1..n into g unordered groups, s.t. prev operation is new/append/join
def solve(n):
    dp = [[[0] * 3 for _ in range(n + 2)] for _ in range(n + 2)]
    dp[1][1][0] = 1

    for n in range(1, n):
        for g in range(1, n + 1):
            # new group
            dp[n + 1][g + 1][0] += sum(dp[n][g])
            dp[n + 1][g + 1][0] %= mod

            # append to existing group
            dp[n + 1][g][1] += dp[n][g][0] * 2 * (g - 1)
            dp[n + 1][g][1] += dp[n][g][1] * (2 * g - 1)
            dp[n + 1][g][1] += dp[n][g][2] * 2 * g
            dp[n + 1][g][1] %= mod

            # join existing groups
            dp[n + 1][g - 1][2] += dp[n][g][0] * (g - 1) * (g - 2)
            dp[n + 1][g - 1][2] += dp[n][g][1] * (g - 1) * (g - 1)
            dp[n + 1][g - 1][2] += dp[n][g][2] * g * (g - 1)
            dp[n + 1][g - 1][2] %= mod

    return sum(dp[n][1]) % mod
