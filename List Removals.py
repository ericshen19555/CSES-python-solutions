def main():
    from sys import stdin
    e = stdin.readline

    n = int(e())
    hb = 1 << n.bit_length() - 1
    l = tuple(map(int, e().split()))
    bit = [i & -i for i in range(n + 1)]
    ans = []
    for v in map(int, e().split()):
        i, b = 0, hb
        while b:
            if i + b <= n and bit[i + b] < v:
                i += b
                v -= bit[i]
            b >>= 1
        ans.append(l[i])
        i += 1
        while i <= n:
            bit[i] -= 1
            i += i & -i
    print(*ans)
main()