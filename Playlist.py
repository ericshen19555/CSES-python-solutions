def main():
    from sys import stdin
    e = stdin.readline

    e()
    l = list(map(int, e().split()))
    d = dict.fromkeys(l, 0)
    ans = cur = 0
    for i, v in enumerate(l):
        c = d[v]
        cur += (c == 0) - (c == 1)
        d[v] += 1
        if ans < cur:
            ans += 1
        else:
            v = l[i - ans]
            d[v] -= 1
            c = d[v]
            cur -= (c == 0) - (c == 1)
    print(ans)
main()