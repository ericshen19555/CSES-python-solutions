def main():
    from sys import stdin
    e = stdin.readline

    n, m = map(int, e().split())
    m += 1
    ws = list(map(int, e().split()))
    vs = list(map(int, e().split()))
    dp = [0] * m
    for w, v in zip(ws, vs):
        for i in range(m - w):
            dp[i] = max(dp[i], dp[i + w] + v)
    print(dp[0])
main()