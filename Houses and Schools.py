def main():
    from sys import stdin
    e = stdin.readline
    inf = 10**20

    n, k = map(int, e().split())
    n += 1
    l = [0] + list(map(int, e().split()))
    li = [0] * n
    for i in range(1, n):
        li[i] = li[i - 1] + l[i] * i
        l[i] += l[i - 1]

    def y(x, line):
        return line[0] * x + line[1]

    def compare_inter_x(a, b, c):
        return (b[1] - a[1]) * (b[0] - c[0]) >= (c[1] - b[1]) * (a[0] - b[0])

    def add(h, line):
        while len(h) >= 2 and compare_inter_x(h[-2], h[-1], line):
            h.pop()
        h.append(line)

    def move(hi, h, x):
        hi = min(hi, len(h) - 1)
        while hi + 1 < len(h) and y(x, h[hi]) > y(x, h[hi + 1]):
            hi += 1
        return hi

    dp = [inf] * n
    dp[0] = 0
    for _ in range(k):
        pp = [inf] * n
        hv = []
        hp = []
        hiv = hip = 0
        for i in range(1, n):
            # pv[i] = min(dp[j] - li[i] + li[j] + l[i] * i - l[j] * i for j in range(i))
            # pp[i] = min(pv[j] + li[i] - li[j] - l[i] * j + l[j] * j for j in range(i + 1))
            # pv[i] = min(dp[j] + li[j] - l[j] * i for j in range(i)) - li[i] + l[i] * i
            # pp[i] = min(pv[j] - li[j] - l[i] * j + l[j] * j for j in range(i + 1)) + li[i]
            add(hp, (-l[i - 1], dp[i - 1] + li[i - 1]))
            hip = move(hip, hp, i)
            dpv = y(i, hp[hip]) - li[i] + l[i] * i
            add(hv, (-i, dpv - li[i] + l[i] * i))
            hiv = move(hiv, hv, l[i])
            pp[i] = y(l[i], hv[hiv]) + li[i]
        dp = pp
    print(dp[-1])
main()
