def main():
    from sys import stdin
    e = stdin.readline

    n, q = map(int, e().split())

    l = [0]
    l.extend(map(int, e().split()))
    for i in range(n, 0, -1):
        l[i] -= l[i - 1]
    for i, v in enumerate(l):
        i += i & -i
        if i <= n:
            l[i] += v

    ans = []
    for _ in range(q):
        o: str = e()
        if o.startswith("1"):
            _, i, j, v = map(int, o.split())
            j += 1
            while i <= n:
                l[i] += v
                i += i & -i
            while j <= n:
                l[j] -= v
                j += j & -j
        else:
            _, i = map(int, o.split())
            res = 0
            ii = i
            while ii > 0:
                res += l[ii]
                ii -= ii & -ii
            ans.append(res)
    print("\n".join(map(str, ans)))
main()