def main():
    from sys import stdin
    mod = 10**9 + 7
    e = stdin.readline

    n = int(e())
    dp = [0] * n
    dp[0] = 1
    for _ in range(n):
        le = 0
        for i, (c, up) in enumerate(zip(e(), dp)):
            if c == '.':
                le = dp[i] = (le + up) % mod
            else:
                le = dp[i] = 0
    print(le)
main()