def main():
    from sys import stdin
    e = stdin.readline

    n, k = map(int, e().split())
    l = list(map(int, e().split()))
    d = dict.fromkeys(l, 0)

    cur = 0
    ans = []
    for i, v in enumerate(l):
        cur += d[v] == 0
        d[v] += 1
        if i >= k:
            p = l[i - k]
            d[p] -= 1
            cur -= d[p] == 0
        if i >= k - 1:
            ans.append(cur)
    print(*ans)
main()