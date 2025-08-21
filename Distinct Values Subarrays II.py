def main():
    from sys import stdin
    e = stdin.readline

    n, k = map(int, e().split())
    l = list(map(int, e().split()))
    cnt = dict.fromkeys(l, 0)
    ans = typ = cur = 0
    nxt = iter(l).__next__
    for v in l:
        typ += (cnt[v] == 0)
        cnt[v] += 1
        cur += 1
        while typ > k:
            p = nxt()
            cnt[p] -= 1
            typ -= (cnt[p] == 0)
            cur -= 1
        ans += cur
    print(ans)
main()