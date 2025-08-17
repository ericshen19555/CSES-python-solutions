def main():
    from sys import stdin
    e = stdin.readline
    ord = dict(zip("ABCD", (0b1110, 0b1101, 0b1011, 0b0111))).__getitem__
    chr = " AB C   D".__getitem__

    m, n = map(int, e().split())
    pre = [15] * n
    ans = [None] * n
    for s in stdin:
        le = 15
        for i, (up, mask) in enumerate(zip(pre, map(ord, s))):
            cur = le & up & mask
            cur &= -cur
            ans[i] = chr(cur)
            le = pre[i] = cur ^ 15
        print("".join(ans))
main()