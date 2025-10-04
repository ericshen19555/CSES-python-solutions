def main():
    from sys import stdin
    from itertools import accumulate
    from operator import xor
    e = stdin.readline

    def fwt(a, inv):
        b = 1
        while b * 2 <= lim:
            for i in range(0, lim, b * 2):
                for j in range(i, i + b):
                    x, y = a[j + 0], a[j + b]
                    a[j + 0] = x + y
                    a[j + b] = x - y
                    if inv:
                        a[j + 0] >>= 1
                        a[j + b] >>= 1
            b <<= 1

    n = int(e())
    l = list(accumulate(map(int, e().split()), xor, initial=0))
    lim = 1 << max(l).bit_length()

    a = [0] * lim
    for v in l:
        a[v] += 1
    zero = max(a) >= 2

    fwt(a, False)
    for i in range(lim):
        a[i] **= 2
    fwt(a, True)

    ans = [i for i in range(lim) if (a[i] if i else zero)]
    print(len(ans))
    print(*ans)
main()