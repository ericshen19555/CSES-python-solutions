def main():
    from sys import stdin
    e = stdin.readline

    ans = []
    for _ in range(int(e())):
        n, k = map(int, e().split())
        if n > k * k:
            ans.append("IMPOSSIBLE")
        else:
            n += 1
            l = []
            for i in range(1, n, k)[::-1]:
                l += range(i, min(n, i + k))
            ans.append(" ".join(map(str, l)))
    print("\n".join(ans))
main()