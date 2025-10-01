def main():
    from sys import stdin
    e = stdin.readline
    n, ans = map(int, e().split())
    l = [int(e(), 2) for _ in range(n)]
    for i in range(1, n):
        v = l[i]
        for j in range(i):
            x = v ^ l[j]
            x -= (x >> 1) & 0x55555555
            x = ((x >> 2) & 0x33333333) + (x & 0x33333333)
            x = ((x >> 4) + x) & 0x0f0f0f0f
            x += x >> 8
            x += x >> 16
            x &= 0x3f
            if x < ans: ans = x
    print(ans)
main()