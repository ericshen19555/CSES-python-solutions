def main():
    from sys import stdin
    from bisect import bisect_left
    from operator import itemgetter
    e = stdin.readline

    n = int(e())
    l = sorted((tuple(map(int, e().split())) for _ in range(n)), key=itemgetter(1))
    dp = [0] * (n + 1)
    end = [0] * (n + 1)
    le = 0
    for i, (s, t, v) in enumerate(l, 1):
        le = dp[i] = max(le, dp[bisect_left(end, s, hi=i) - 1] + v)
        end[i] = t
    print(le)
main()