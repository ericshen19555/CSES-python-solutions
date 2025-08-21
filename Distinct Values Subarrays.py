def main():
    from sys import stdin
    from itertools import tee
    e = stdin.readline

    e()
    l, p = tee(map(int, e().split()))
    nxt = p.__next__
    u = set()
    ans = cur = 0
    for v in l:
        if v in u:
            while (p := nxt()) != v:
                u.remove(p)
                cur -= 1
        else:
            cur += 1
            u.add(v)
        ans += cur
    print(ans)
main()