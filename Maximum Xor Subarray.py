def main():
    from sys import stdin
    from itertools import accumulate
    from operator import xor
    e = stdin.readline

    n = int(e())
    l = list(accumulate(map(int, e().split()), func=xor, initial=0))
    ans = 0
    b, mask = 1 << 29, -1 << 29
    while b:
        t = ans | b
        p = {v & mask for v in l}
        for v in p:
            if v ^ t in p:
                ans = t
                break
        b >>= 1
        mask >>= 1
    print(ans)
main()