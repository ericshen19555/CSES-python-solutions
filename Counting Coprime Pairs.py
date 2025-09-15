def main():
    from sys import stdin
    e = stdin.readline
    lim = 10**6 + 1

    e()  # n
    freq = [0] * lim
    for v in map(int, e().split()):
        freq[v] += 1

    f = [0] * lim
    for d in range(1, lim):
        for m in range(d, lim, d):
            f[d] += freq[m]
        f[d] = f[d] * (f[d] - 1) >> 1

    for d in range(lim - 1, 0, -1):
        for m in range(d << 1, lim, d):
            f[d] -= f[m]
    print(f[1])
main()