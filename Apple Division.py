def main():
    from sys import stdin
    from itertools import islice
    from bisect import bisect_left
    e = stdin.readline

    n = int(e())
    l = map(int, e().split())
    le = n >> 1; ri = n - le
    sub1 = [0]
    for v in islice(l, le):
        for x in islice(sub1, len(sub1)):
            sub1.append(x + v)
    sub2 = [0]
    for v in l:
        for x in islice(sub2, len(sub2)):
            sub2.append(x + v)
    s = sub1[-1] + sub2[-1]; t = s >> 1
    sub2.sort()
    ans = float("INF")
    for v in sub1:
        i = bisect_left(sub2, t - v)
        if i < (1 << ri): ans = min(ans, abs(2 * (v + sub2[i]) - s))
        i += 1
        if i < (1 << ri): ans = min(ans, abs(2 * (v + sub2[i]) - s))
    print(ans)
main()