def main():
    from sys import stdin
    e = stdin.readline
    e()
    l = list(map(int, e().split()))
    m = max(l)
    print(m + max(m, sum(l) - m))
main()