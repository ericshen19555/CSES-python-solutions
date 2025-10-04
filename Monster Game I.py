def main():
    from sys import stdin
    e = stdin.readline

    p = [0]
    n, p[0] = map(int, e().split())
    l = list(map(int, e().split()))
    p += list(map(int, e().split()))

    def y(i, x):
        return dp[i] + x * p[i]

    def compare_inter_x(i, j, k):
        dx1, dy1 = p[i] - p[j], dp[j] - dp[i]
        dx2, dy2 = p[j] - p[k], dp[k] - dp[j]
        return dy1 * dx2 >= dy2 * dx1

    dp = [0] * (n + 1)
    hi = 0
    h = [0]
    for i in range(1, n + 1):
        v = l[i - 1]
        while hi + 1 < len(h) and y(h[hi], v) > y(h[hi + 1], v):
            hi += 1
        dp[i] = y(h[hi], v)
        while len(h) >= 2 and compare_inter_x(h[-2], h[-1], i):
            h.pop()
        h.append(i)
    print(dp[n])
main()