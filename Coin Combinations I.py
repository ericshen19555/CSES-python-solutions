def main():
    from sys import stdin
    mod = 10**9 + 7
    e = stdin.readline

    n, m = map(int, e().split())
    m += 1
    dp = [0] * m
    dp[0] = 1
    l = sorted(map(int, e().split()))
    for i in range(m):
        x = dp[i] % mod
        for v in l:
            v += i
            if v >= m: break
            dp[v] += x
    print(x)
main()