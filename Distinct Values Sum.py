def main():
    from sys import stdin
    e = stdin.readline

    n = int(e())
    l = list(map(int, e().split()))

    last = {}
    ans = cur = 0
    for i, v in enumerate(l, 1):
        cur += i - last.get(v, 0)
        last[v] = i
        ans += cur
    print(ans)
main()