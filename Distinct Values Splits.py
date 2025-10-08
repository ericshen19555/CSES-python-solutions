def main():
    from sys import stdin
    e = stdin.readline
    mod = 10**9 + 7

    n = int(e())
    l = list(map(int, e().split()))

    j = 0
    vis = set()
    dp = [0] * (n + 1)
    dp[-1] = cur = 1
    for i, v in enumerate(l):
        while v in vis:
            vis.remove(l[j])
            cur -= dp[j - 1]
            j += 1
        vis.add(v)
        cur %= mod
        dp[i] = cur
        cur <<= 1
    print(dp[n - 1])
main()
