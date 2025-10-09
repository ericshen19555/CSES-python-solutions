def main():
    from sys import stdin
    e = stdin.readline

    n = int(e())
    l = [tuple(map(int, e().split())) for _ in range(n)]
    l.sort()

    def cross(o, a, b):
        return (l[a][0] - l[o][0]) * (l[b][1] - l[o][1]) - (l[a][1] - l[o][1]) * (l[b][0] - l[o][0])

    h = []
    for i in range(n):
        while len(h) >= 2 and cross(h[-2], h[-1], i) < 0:
            h.pop()
        h.append(i)
    lo = len(h)
    for i in range(n - 2, -1, -1):
        while len(h) > lo and cross(h[-2], h[-1], i) < 0:
            h.pop()
        h.append(i)
    h.pop()

    ans = [f"{len(h)}"]
    for i in h:
        ans.append(f"{l[i][0]} {l[i][1]}")
    print("\n".join(ans))
main()