def main():
    from sys import stdin
    from operator import itemgetter
    from bisect import bisect_right, insort
    e = stdin.readline

    def expand(i):
        chunk = sl[i]
        if len(chunk) <= (s << 1): return
        sl.insert(i + 1, chunk[s:])
        mn.insert(i + 1, chunk[s])
        del chunk[s:]

    n, k = map(int, e().split())
    l = [tuple(map(int, e().split())) for _ in range(n)]
    l.sort(key=itemgetter(1))
    ans = 0
    s = int(k ** 0.5)
    sl = []
    i = 0
    for i in range(s, k, s):
        sl.append([0] * s)
    if i < k:
        sl.append([0] * (k - i))
    mn = [0] * len(sl)
    for a, b in l:
        i = bisect_right(mn, a) - 1
        if i == -1: continue
        chunk = sl[i]
        j = bisect_right(chunk, a) - 1
        if j == -1: continue

        ans += 1

        del chunk[j]
        if len(chunk) > (s >> 1):
            mn[i] = chunk[0]
        elif len(sl) > 1:
            if i: i -= 1
            sl[i].extend(sl[i + 1])
            del sl[i + 1]
            del mn[i + 1]
            expand(i)

        i = bisect_right(mn, b)
        if i: i -= 1
        insort(sl[i], b)
        expand(i)
    print(ans)
main()
