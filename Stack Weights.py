def main():
    from sys import stdin
    e = stdin.readline

    n = int(e())
    m = 1 << n.bit_length()
    mx = [0] * (m << 1)
    mn = [0] * (m << 1)
    tag = [0] * (m << 1)

    def ctz(x):
        return (x & -x).bit_length() - 1

    ans = []
    for _ in range(n):
        i, v = map(int, e().split())
        v = 1 if v == 1 else -1
        x = m + i
        while x:
            x = (x >> ctz(x)) - 1
            tag[x] += v
        x = m + i
        while x:
            x >>= 1
            mx[x] = max(mx[x << 1] + tag[x << 1], mx[x << 1 | 1] + tag[x << 1 | 1])
            mn[x] = min(mn[x << 1] + tag[x << 1], mn[x << 1 | 1] + tag[x << 1 | 1])
        ans.append("<" if mx[1] <= 0 else ">" if mn[1] >= 0 else "?")
    print("\n".join(ans))
main()