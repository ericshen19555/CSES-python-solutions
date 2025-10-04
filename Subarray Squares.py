def main():
    from sys import stdin
    from itertools import accumulate
    e = stdin.readline
    inf = 10**20

    n, k = map(int, e().split())
    n, k = n + 1, k + 1
    l = list(accumulate(map(int, e().split()), initial=0))

    def y(x, line):
        return line[0] * x + line[1]

    def compare_inter_x(a, b, c):
        return (b[1] - a[1]) * (b[0] - c[0]) >= (c[1] - b[1]) * (a[0] - b[0])

    def add(line):
        while len(h) >= 2 and compare_inter_x(h[-2], h[-1], line):
            h.pop()
        h.append(line)

    make_line = lambda v, x: (-v << 1, x + v ** 2)

    dp = [inf] * n
    dp[0] = 0
    for kk in range(1, k):
        h = []
        hi = 0
        add(make_line(0, dp[0]))
        dp[0] = inf
        for i in range(1, n):
            # p[i] = min(d[j] + (l[i] - l[j]) ** 2 for j in range(i))
            up, v = dp[i], l[i]
            hi = min(hi, len(h) - 1)
            while hi + 1 < len(h) and y(v, h[hi]) > y(v, h[hi + 1]):
                hi += 1
            dp[i] = (h[hi][0] + v) * v + h[hi][1]
            add(make_line(v, up))
    print(dp[-1])
main()
