def main():
    from sys import stdin
    from bisect import bisect_left
    e = stdin.readline

    n, k = map(int, e().split())
    l = list(map(int, e().split()))
    sl = sorted(l)
    for i, v in enumerate(sl):
        if (v << 1) > k:
            print("IMPOSSIBLE")
            return
        j = bisect_left(sl, k - v, lo=i + 1)
        if j < n and sl[j] + v == k: break
    else:
        print("IMPOSSIBLE")
        return
    i = l.index(v)
    print(i + 1, l.index(k - v, i + 1 if v << 1 == k else 0) + 1)
main()