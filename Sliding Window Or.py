def main():
    from sys import stdin
    e = stdin.readline

    n, k = map(int, e().split())
    x, a, b, c = map(int, e().split())
    m = n - k + 1

    l = [0] * n
    for i in range(n):
        l[i] = x
        x = (a * x + b) % c

    ans = 0
    for s in range(0, m, k):
        for i in range(s + k - 1, s, -1):
            l[i - 1] |= l[i]
        cur = 0
        for i in range(s, min(m, s + k)):
            cur |= l[i + k - 1]
            ans ^= l[i] | cur
    print(ans)
main()