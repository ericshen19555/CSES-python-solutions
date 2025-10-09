def main():
    from sys import stdin
    from random import randint
    e = stdin.readline
    LOAD = 3
    shift = 10 ** 9 + randint(114514, 1919810)

    n = int(e())
    l = []
    for _ in range(n):
        a, b = map(int, e().split())
        a, b = a + shift, b + shift
        l.append(a * b << 64 | a << 32 | b)
    l.sort()

    ans = float("INF")
    for i in range(n):
        x = l[i]
        a, b = (x >> 32) & 0xffffffff, x & 0xffffffff
        l[i] = a, b = a - shift, b - shift
        for j in range(max(0, i - LOAD), i):
            c, d = l[j]
            ans = min(ans, (a - c) ** 2 + (b - d) ** 2)
    print(ans)
main()