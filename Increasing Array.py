def main():
    from sys import stdin
    from itertools import accumulate, tee
    e = stdin.readline

    e()
    a, b = tee(map(int, e().split()))
    print(sum(map(int.__sub__, accumulate(a, max), b)))
main()