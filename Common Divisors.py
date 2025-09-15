def main():
    from sys import stdin
    e = stdin.readline

    lim = 10**6 + 1

    n = int(e())
    freq = [0] * lim
    for v in map(int, e().split()):
        freq[v] += 1

    for d in reversed(range(lim)):
        cnt = 0
        for m in range(d, lim, d):
            cnt += freq[m]
            if cnt >= 2:
                print(d)
                return

    print(1)
main()
