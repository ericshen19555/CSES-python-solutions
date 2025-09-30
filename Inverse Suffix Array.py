def main():
    from sys import stdin
    e = stdin.readline

    n = int(e())
    sa = [int(v) - 1 for v in e().split()]
    rk = [0] * (n + 1)
    for i, v in enumerate(sa):
        rk[v] = i

    s = [0] * n
    a = sa[0]
    s[a] = c = ord("a")
    for i in range(1, n):
        b = sa[i]
        if rk[a + 1] > rk[b + 1]:
            c += 1
            if c > ord("z"):
                return print(-1)
        s[b] = c
        a = b
    print("".join(map(chr, s)))
main()