def main():
    from sys import stdin
    e = stdin.readline

    n = int(e())
    a = list(map(int, e().split()))
    b = list(map(int, e().split()))

    ans = x = y = 0
    for i in range(n):
        x += a[i] - 1
        y += b[i] - 1
        d = 0
        if x < 0 < y:
            d = min(-x, y)
        elif x > 0 > y:
            d = max(-x, y)
        x += d
        y -= d
        ans += abs(d) + abs(x) + abs(y)
    print(ans)
main()