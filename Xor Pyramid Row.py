def main():
    from sys import stdin
    e = stdin.readline

    n, k = map(int, e().split())
    l = list(map(int, e().split()))

    b = n - k
    while b:
        lb = b & -b
        for i in range(n - lb):
            l[i] ^= l[i + lb]
        b &= b - 1
    print(*l[:k])
main()