def main():
    from sys import stdin
    from itertools import accumulate
    e = stdin.readline

    n = int(e())

    def cross(a, b, o):
        return (o[0] - a[0]) * (o[1] - b[1]) - (o[1] - a[1]) * (o[0] - b[0])

    h = [(-1, 0)]
    ans = [0] * n
    for i, v in enumerate(accumulate(map(int, e().split()))):
        o = (i, v)
        while len(h) >= 2 and cross(h[-2], h[-1], o) <= 0:
            h.pop()
        ans[i] = i - h[-1][0]
        h.append(o)
    print(*ans)
main()