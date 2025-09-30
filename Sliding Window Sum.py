def main():
    from sys import stdin
    e = stdin.readline

    n, k = map(int, e().split())
    x, a, b, c = map(int, e().split())

    cur = 0
    p = v = x
    for i in range(k):
        cur += v
        v = (a * v + b) % c
    ans = cur
    for i in range(n - k):
        cur -= p
        cur += v
        ans ^= cur
        p = (a * p + b) % c
        v = (a * v + b) % c
    print(ans)
main()