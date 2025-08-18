def main():
    from sys import stdin
    e = stdin.readline

    n = int(e())
    l = sorted(map(int, e().split()))
    mid = l[n >> 1]
    print(sum(abs(v - mid) for v in l))
main()