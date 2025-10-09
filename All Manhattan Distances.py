def main():
    from sys import stdin
    e = stdin.readline

    n = int(e())
    xs = [0] * n
    ys = [0] * n
    for i in range(n):
        xs[i], ys[i] = map(int, e().split())
    xs.sort(), ys.sort()

    ans = cur = 0
    px = py = 0
    for i in range(n):
        x, y = xs[i], ys[i]
        cur += (x - px + y - py) * i
        ans += cur
        px, py = x, y
    print(ans)
main()