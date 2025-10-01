def main():
    from sys import stdin
    from collections import Counter
    e = stdin.readline

    n, k = map(int, e().split())
    l = list(map(int, e().split()))
    half = n >> 1
    a = [0]
    for v in l[:half]:
        a += [s + v for s in a]
    c = Counter(a)

    b = [0]
    for v in l[half:]:
        b += [s + v for s in b]
    print(sum(c.get(k - v, 0) for v in b))
main()
