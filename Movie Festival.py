def main():
    from sys import stdin
    from operator import itemgetter
    e = stdin.readline

    n = int(e())
    l = [tuple(map(int, e().split())) for _ in range(n)]
    l.sort(key=itemgetter(1))

    ans = pre = 0
    for s, t in l:
        if pre <= s:
            ans += 1
            pre = t
    print(ans)
main()