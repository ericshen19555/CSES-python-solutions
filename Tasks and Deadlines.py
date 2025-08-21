def main():
    from sys import stdin
    from itertools import accumulate
    e = stdin.readline

    n = int(e())
    ans = 0
    l = [0] * n
    for i in range(n):
        a, d = map(int, e().split())
        l[i] = a
        ans += d
    l.sort()
    print(ans - sum(accumulate(l)))
main()